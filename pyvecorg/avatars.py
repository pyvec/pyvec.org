import io
from urllib.parse import quote
import hashlib

from PIL import Image, ImageFilter
import requests


def get_avatar_url(member):
    key = member.get('avatar') or 'email'  # defaults to 'email'
    value = member.get(key)

    if value:
        if key == 'email':
            hash = hashlib.md5(value.lower().strip().encode()).hexdigest()
            return f'https://www.gravatar.com/avatar/{hash}?size=100&d=404'
        elif key == 'github':
            username = quote(value)
            return f'https://github.com/{username}.png'

    # to disable avatar, specify it as 'none' or basically anything invalid
    return 'https://www.gravatar.com/avatar/0000?d=mm&f=y'


def create_thumbnail(file, size):
    image = Image.open(file)

    image.convert('RGB')
    image.thumbnail((size, size))
    image.filter(ImageFilter.SHARPEN)

    binary = io.BytesIO()
    image.save(binary, 'PNG')
    binary.seek(0)

    return binary
