import re
import os
import hashlib
import textwrap
from urllib.parse import quote

import jinja2
import requests
from markdown import markdown

from pyvecorg import app


@app.template_filter('markdown')
def convert_markdown(text):
    text = textwrap.dedent(text)
    result = jinja2.Markup(markdown(text))
    return result


@app.template_filter('avatar_url')
def get_avatar_url(member):
    no_avatar = 'https://www.gravatar.com/avatar/0000?d=mm&f=y'

    try:
        key = member['avatar']
        value = member[key]
    except KeyError:
        return no_avatar

    if key == 'email':
        email_hash = hashlib.md5(value.lower().strip().encode()).hexdigest()
        return f'https://www.gravatar.com/avatar/{email_hash}?size=400&d=404'
    elif key == 'twitter':
        if os.getenv('DISABLE_TWITTER_AVATARS'):
            return no_avatar
        username = quote(value)
        url = f'https://twitter.com/{username}/profile_image'
        url = requests.head(url).headers.get('location')
        return url.replace('_normal', '_400x400')
    if key == 'github':
        username = quote(value)
        return f'https://github.com/{username}.png'

    return no_avatar


@app.template_filter('url')
def normalize_url(url):
    return re.sub(r'^https?://', '', url).rstrip('/')


@app.template_filter('format_number')
def format_number(number):
    if 'sum' in number:
        n = sum(number['sum'])
    else:
        n = number['value']

    if number.get('exactly'):
        return str(n)

    digits = len(str(int(n)))
    if digits > 2:
        order = 10 ** (digits - 2)
        n = (n // order) * order
    if digits == 2:
        n = (n // 10) * 10

    return f'{n}+'
