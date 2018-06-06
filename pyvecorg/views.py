import os
from datetime import datetime

from flask import (request, render_template, redirect, url_for,
                   send_from_directory)

from pyvecorg import app
from pyvecorg.data import load_data, select_language


data = load_data()


@app.route('/')
def index_redirect():
    if request.accept_languages.best_match(['en', 'cs', 'sk']) == 'en':
        return redirect(url_for('index', lang='en'))
    return redirect(url_for('index', lang='cs'))


@app.route('/favicon.ico')
def favicon():
    static = os.path.join(app.root_path, 'static')
    return send_from_directory(static, 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/<lang>/')
def index(lang):
    context = select_language(data, lang)
    context['lang'] = lang
    context['now'] = datetime.now()
    return render_template('index.html', **context)
