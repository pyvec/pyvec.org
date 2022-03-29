import re
import textwrap

from markdown import markdown
from markupsafe import Markup

from pyvecorg import app


@app.template_filter('markdown')
def convert_markdown(text):
    text = textwrap.dedent(text)
    result = Markup(markdown(text))
    return result


@app.template_filter('url')
def normalize_url(url):
    return re.sub(r'^https?://', '', url).rstrip('/')


def floor_number(n):
    digits = len(str(int(n)))
    if digits > 2:
        order = 10 ** (digits - 2)
        n = (n // order) * order
    if digits == 2:
        n = (n // 10) * 10
    return n


def choose_plural(text, n):
    """
    Chooses the Czech plural form based on n.
    This either gets and immediately returns a string,
    or it gets a list of 3 strings:

     * for 1 item
     * for 2-4 items
     * for the rest

    Picks the right one and returns it.

    Uses the more modern option where e.g. 21 is NOT pluralized as 1
    http://prirucka.ujc.cas.cz/?id=792
    """
    if isinstance(text, str):
        return text

    # we don't expect negative numbers here, but just to be sure
    n = abs(n)

    if n == 1:
        return text[0]
    if 1 < n < 5:
        return text[1]
    return text[2]


@app.template_filter('format_number_text')
def format_number_text(number):
    if 'sum' in number:
        n = sum(number['sum'])
    else:
        n = number['value']

    if not number.get('exactly'):
        n = floor_number(n)
        plus = '+'
    else:
        plus = ''

    text = choose_plural(number['text'], n)

    return f'{n}{plus} {text}'
