import io
import os
import json
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
    for row in rows:
        if frozenset(['name', 'role', 'avatar']) < frozenset(row):
            head = row
            break
    for row in rows:
        yield {key: value for key, value in zip(head, row) if value != ''}


def generate_yaml(data):
    yaml_contents = '''\
#
#  This file has been generated from external sources
#  using `pipenv run build`. Do not edit it manually!
#
'''
    return yaml_contents + yaml.dump(data, allow_unicode=True)


if __name__ == '__main__':
    # Build data/members_list.yml and avatar images
    gsa_path = PACKAGE_DIR / 'google_service_account.json'
    gsa_json = os.getenv('GOOGLE_SERVICE_ACCOUNT') or gsa_path.read_text()
    gsa = json.loads(gsa_json)

    doc_key = '1n8hzBnwZ5ANkUCvwEy8rWsXlqeAAwu-5JBodT5OJx_I'
    rows = read_spreadsheet(doc_key, 'list', gsa)
    members = [member for member in parse_members(rows)
               if member.get('role') in ('board', 'chair')]

    AVATARS_DIR.mkdir(exist_ok=True)
    for member in members:
        avatar_url = get_avatar_url(member)
        img_basename = slugify(member['name']) + '.png'

        response = requests.get(avatar_url)
        response.raise_for_status()
        img_bytes = create_thumbnail(io.BytesIO(response.content), 100).read()

        img_path = (AVATARS_DIR / img_basename)
        img_path.write_bytes(img_bytes)

        member['avatar_filename'] = str(img_path.relative_to(STATIC_DIR))

    data = dict(entries=list(members))
    MEMBERS_LIST_YAML.write_text(generate_yaml(data))
