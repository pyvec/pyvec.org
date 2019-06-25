import csv
from pathlib import Path

import yaml
import requests


MEMBERS_LIST_YAML = Path(__file__).parent / 'data' / 'members_list.yml'
CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSWK18MlEy95sAGl1BM6BXWxPgJbIx2UH3tAyJjxES06hHuaXgpsmD5pRz9kkGcFupiZL_U_e7yv4t1/pub?gid=0&single=true&output=csv'  # noqa


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
    # Build data/members_list.yml
    response = requests.get(CSV_URL)
    response.raise_for_status()
    members = parse_members_csv(response.content.decode('utf-8'))
    data = dict(entries=list(members))
    MEMBERS_LIST_YAML.write_text(generate_yaml(data))
