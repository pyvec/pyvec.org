import io
import csv
from pathlib import Path

import yaml
import requests
from slugify import slugify

from pyvecorg.avatars import get_avatar_url, create_thumbnail


MEMBERS_LIST_YAML = Path(__file__).parent / 'data' / 'members_list.yml'
MEMBERS_CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSWK18MlEy95sAGl1BM6BXWxPgJbIx2UH3tAyJjxES06hHuaXgpsmD5pRz9kkGcFupiZL_U_e7yv4t1/pub?gid=0&single=true&output=csv'  # noqa
STATIC_DIR = Path(__file__).parent / 'static'
AVATARS_DIR = STATIC_DIR / 'img' / 'avatars'


def parse_members_csv(content):
    lines = content.splitlines()
    rows = csv.reader(lines, delimiter=',')

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
    response = requests.get(MEMBERS_CSV_URL)
    response.raise_for_status()

    members = [
        member for member
        in parse_members_csv(response.content.decode('utf-8'))
        if member.get('role')  # currently we only display members with role
    ]

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
