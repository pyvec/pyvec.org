import io
from urllib.parse import quote
import hashlib

from PIL import Image, ImageFilter
import requests


def get_avatar_url(member):
    no_avatar = 'https://www.gravatar.com/avatar/0000?d=mm&f=y'
    try:
        key = member['avatar']
        value = member[key]
    except KeyError:
        return no_avatar

    if key == 'email':
        email_hash = hashlib.md5(value.lower().strip().encode()).hexdigest()
        return f'https://www.gravatar.com/avatar/{email_hash}?size=100&d=404'
    elif key == 'twitter':
        username = quote(value)
        url = f'https://twitter.com/{username}/profile_image'
        url = requests.head(url).headers.get('location')
        return url.replace('_normal', '_200x200')
    if key == 'github':
        username = quote(value)
        return f'https://github.com/{username}.png'


def create_thumbnail(file, size):
    image = Image.open(file)

    image.convert('RGB')
    image.thumbnail((size, size))
    image.filter(ImageFilter.SHARPEN)

    binary = io.BytesIO()
    image.save(binary, 'PNG')
    binary.seek(0)

    return binary
