import os
from setuptools.command.egg_info import FileList

from flask import Flask as BaseFlask


# Makes sure everything included in the package is watched for changes
# by the development server. See https://github.com/pyvec/elsa/issues/43
class Flask(BaseFlask):
    pkg_root = os.path.join(os.path.dirname(__file__), '..')
    manifest = os.path.join(pkg_root, 'MANIFEST.in')

    def run(self, *args, **kwargs):
        file_list = FileList()
        with open(self.manifest) as f:
            for line in f.readlines():
                file_list.process_template_line(line)
        kwargs['extra_files'] = [os.path.join(self.pkg_root, path)
                                 for path in file_list.files]
        return super().run(*args, **kwargs)


app = Flask('pyvecorg')

from pyvecorg import views  # NOQA
from pyvecorg import templating  # NOQA
