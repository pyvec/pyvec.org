import io
from urllib.parse import quote
import hashlib

from PIL import Image, ImageFilter
import requests


def get_avatar_url(member):
    key = member.get('avatar') or 'github'  # defaults to 'github'
    value = member.get(key)

    if value:
        if key == 'email':
            hash = hashlib.md5(value.lower().strip().encode()).hexdigest()
            return f'https://www.gravatar.com/avatar/{hash}?size=100&d=404'
        elif key == 'twitter':
            username = quote(value)
            url = f'https://twitter.com/{username}/profile_image'
            url = requests.head(url, headers={
                # Twitter now only allows Googlebot to fetch avatars (facepalm)
                'User-Agent': 'Googlebot/42 (+http://www.google.com/bot.html)',
            }).headers.get('location')
            return url.replace('_normal', '_200x200')
        if key == 'github':
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
