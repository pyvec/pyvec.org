import io
from urllib.parse import quote
import hashlib

from PIL import Image, ImageFilter
import requests


def get_avatar_url(member):
    key = member.get('avatar') or 'email'  # defaults to 'email'
    value = member.get(key)

    if value:
        if key == 'github':
            username = quote(value)
            return f'https://github.com/{username}.png'
        if key == 'email':
            url = get_gravatar_url(value)
            # if the person has set a gravatar, the function returns the URL
            # else this falls back to the default gravatar URL below
            if url:
                return url

    # to disable avatar, specify it as 'none' or basically anything invalid
    return 'https://www.gravatar.com/avatar/0000?d=mm&f=y'


def get_gravatar_url(email):
    hash = hashlib.md5(email.lower().strip().encode()).hexdigest()
    url = f'https://www.gravatar.com/avatar/{hash}?size=100&d=404'
    try:
        requests.head(url).raise_for_status()
        return url
    except:
        return None


def create_thumbnail(file, size):
    image = Image.open(file)

    image.convert('RGB')
    image.thumbnail((size, size))
    image.filter(ImageFilter.SHARPEN)

    binary = io.BytesIO()
    image.save(binary, 'PNG')
    binary.seek(0)

    return binary
