import os

import yaml


DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
SUPPORTED_LANGS = {'cs', 'en'}


def load_data():
    data = {}
    for basename in os.listdir(DATA_PATH):
        name, ext = os.path.splitext(basename)
        if ext in ['.yml', '.yaml']:
            with open(os.path.join(DATA_PATH, basename)) as f:
                data[name] = yaml.load(f)
    return data


def select_language(data, lang):
    if lang not in SUPPORTED_LANGS:
        raise ValueError(f"Unsupported language: '{lang}'")

    if isinstance(data, dict):
        keys = list(data.keys())
        if frozenset(keys) <= SUPPORTED_LANGS:
            try:
                return data[lang]
            except KeyError:
                return None
        else:
            return dict(
                [(key, select_language(data[key], lang)) for key in keys])
    elif isinstance(data, list):
        return [select_language(item, lang) for item in data]
    else:
        return data
