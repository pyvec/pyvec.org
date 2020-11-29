import pytest

from pyvecorg import templating


@pytest.mark.parametrize('expected', ['0 hadů', '1 had', '2 hadi', '4 hadi',
                                      '5 hadů', '9 hadů', '10 hadů', '13 hadů',
                                      '19 hadů', '20 hadů', '1111 hadů',
                                      '21 hadů', '22 hadů', '25 hadů',
                                      '881 hadů', '884 hadů', '888 hadů'])
def test_choosing_plural_form(expected):
    forms = ['had', 'hadi', 'hadů']
    n, *_ = expected.partition(' ')
    text = templating.choose_plural(forms, int(n))
    assert f'{n} {text}' == expected
