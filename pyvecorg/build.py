import io
import os
import json
from textwrap import dedent
from pathlib import Path

import yaml
import requests
from slugify import slugify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from pyvecorg.avatars import get_avatar_url, create_thumbnail


PACKAGE_DIR = Path(__file__).parent
MEMBERS_LIST_YAML = PACKAGE_DIR / 'data' / 'members_list.yml'
MEMBERS_CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSWK18MlEy95sAGl1BM6BXWxPgJbIx2UH3tAyJjxES06hHuaXgpsmD5pRz9kkGcFupiZL_U_e7yv4t1/pub?gid=0&single=true&output=csv'  # noqa
STATIC_DIR = PACKAGE_DIR / 'static'
AVATARS_DIR = STATIC_DIR / 'img' / 'avatars'


def read_spreadsheet(doc_key, sheet_name, google_service_account):
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        google_service_account,
        [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive',
        ]
    )
    doc = gspread.authorize(credentials).open_by_key(doc_key)
    return doc.worksheet(sheet_name).get_all_values()


def parse_members(rows):
    head = None
    rows = iter(rows)
    for row in rows:
        if frozenset(['name', 'role', 'avatar']) < frozenset(row):
            head = row
            break
    for row in rows:
        yield {key: value for key, value in zip(head, row) if value != ''}


def coerce_member(member):
    return {
        'name': member.get('nickname', member.get('name')),
        'role': member.get('role'),
        'github': member.get('github'),
        'twitter': member.get('twitter'),
        'linkedin': member.get('linkedin'),
        'avatar_filename': member.get('avatar_filename'),
    }


def generate_yaml(data):
    yaml_contents = dedent('''\
        #
        #  This file has been generated from external sources
        #  using `pipenv run build`. Do not edit it manually!
        #
    ''')
    return yaml_contents + yaml.dump(data, allow_unicode=True)


def create_member_sorting_key(member):
    return (
        0 if member.get('role') == 'chair' else 1,  # chair to be first
        member.get('nickname', member['name']).split(' ')[-1],  # last name
    )


def is_board(member):
    return member.get('role') in ('board', 'chair')


def is_public_member(member):
    return not is_board(member) and member.get('gdpr_consent') == 'yes'


if __name__ == '__main__':
    # Build data/members_list.yml and avatar images
    gsa_path = PACKAGE_DIR / 'google_service_account.json'
    gsa_json = os.getenv('GOOGLE_SERVICE_ACCOUNT') or gsa_path.read_text()
    gsa = json.loads(gsa_json)

    # Document key appears in the URL if you have the document open
    # in your browser
    doc_key = '1n8hzBnwZ5ANkUCvwEy8rWsXlqeAAwu-5JBodT5OJx_I'
    rows = read_spreadsheet(doc_key, 'list', gsa)
    members = list(sorted([
        member for member in parse_members(rows)
    ], key=create_member_sorting_key))

    AVATARS_DIR.mkdir(exist_ok=True)
    for member in members:
        if is_board(member) or is_public_member(member):
            avatar_url = get_avatar_url(member)
            img_basename = slugify(member['name']) + '.png'

            response = requests.get(avatar_url)
            response.raise_for_status()
            response_bytes = io.BytesIO(response.content)
            img_bytes = create_thumbnail(response_bytes, 100).read()

            img_path = (AVATARS_DIR / img_basename)
            img_path.write_bytes(img_bytes)

            member['avatar_filename'] = str(img_path.relative_to(STATIC_DIR))

    data = dict(board=[coerce_member(member) for member in members
                       if is_board(member)],
                public_members=[coerce_member(member) for member in members
                                if is_public_member(member)],
                total_count=len(members))
    MEMBERS_LIST_YAML.write_text(generate_yaml(data))
