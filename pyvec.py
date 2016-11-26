import textwrap

from flask import Flask, render_template
import jinja2
from markdown import markdown

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/en/')
def index_en():
    return render_template('index_en.html')


@app.template_filter('markdown')
def convert_markdown(text):
    text = textwrap.dedent(text)
    result = jinja2.Markup(markdown(text))
    return result


if __name__ == '__main__':
    from elsa import cli
    cli(app, base_url='https://example.com')
