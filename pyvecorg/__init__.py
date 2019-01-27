import os
import itertools
from pathlib import Path

from flask import Flask as BaseFlask


class Flask(BaseFlask):
    # Elsa watches only Python files by default, this adds certain directories
    # https://github.com/pyvec/elsa/issues/43
    extra_dirs = ['data', 'static', 'templates']

    def run(self, *args, **kwargs):
        pyvecorg_dir = Path(__file__).parent
        extra_files = [
            str(path) for path
            in itertools.chain.from_iterable([
                pyvecorg_dir.glob(dir + '/**/*') for dir
                in self.extra_dirs
            ])
        ]
        kwargs['extra_files'] = extra_files
        return super().run(*args, **kwargs)


app = Flask('pyvecorg')
app.config['JSON_AS_ASCII'] = False


from pyvecorg import views
from pyvecorg import templating


__all__ = ['app', 'views', 'templating']
