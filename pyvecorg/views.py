import os
import io
import platform
from datetime import datetime

from flask import (request, render_template, redirect, url_for,
                   send_from_directory, jsonify, abort, send_file)
from slugify import slugify
import requests

from pyvecorg import app
from pyvecorg.avatars import get_avatar_url, create_thumbnail
from pyvecorg.data import load_data, select_language


data = load_data()


@app.route('/favicon.ico')
def favicon():
    static = os.path.join(app.root_path, 'static')
    mimetype = ('image/x-icon' if platform.system() == 'Darwin'
                else 'image/vnd.microsoft.icon')
    return send_from_directory(static, 'favicon.ico',
                               mimetype=mimetype)


@app.route('/')
def index_redirect():
    return redirect(url_for('index', lang='cs'))


@app.route('/<lang>/')
def index(lang):
    context = select_language(data, lang)
    context['lang'] = lang
    context['now'] = datetime.now()
    return render_template('index.html', **context)


@app.route('/<lang>/api.json')
def api(lang):
    return jsonify(select_language(data, lang))


@app.route('/static/img/avatars/<name>.png')
def avatar(name):
    try:
        member = [member for member in data['members']['entries']
                  if slugify(member['name']) == name][0]
    except IndexError:
        abort(404)

    url = get_avatar_url(member)
    res = requests.get(url)
    res.raise_for_status()
    file = create_thumbnail(io.BytesIO(res.content), 100)

    return send_file(file, mimetype='image/png', as_attachment=True,
                           attachment_filename=f'{name}.png')
