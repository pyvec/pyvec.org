import os
import platform
from datetime import datetime

from flask import (render_template, redirect, url_for, send_from_directory,
                   jsonify)

from pyvecorg import app
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
    context['this'] = 'index'
    return render_template('index.html', **context)


@app.route('/en/privacy-policy/', defaults={'lang': 'en'})
@app.route('/cs/zpracovani-osobnich-udaju/', defaults={'lang': 'cs'})
def privacy_policy(lang):
    context = select_language(data, lang)
    context['lang'] = lang
    context['this'] = 'privacy_policy'
    return render_template('privacy_policy.html', **context)


@app.route('/<lang>/api.json')
def api(lang):
    return jsonify(select_language(data, lang))

@app.route('/en/coc/', defaults={'lang': 'en'})
@app.route('/cs/kodex-chovani/', defaults={'lang': 'cs'})
def coc(lang):
    context = select_language(data, lang)
    context['lang'] = lang
    context['this'] = 'coc'
    return render_template('coc.html', **context)