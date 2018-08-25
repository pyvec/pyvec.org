import os

import yaml
import pipfile


def test_python_version():
    project_dir = os.path.join(os.path.dirname(__file__), '..')

    with open(os.path.join(project_dir, '.travis.yml')) as f:
        travis_py_version = yaml.load(f)['python'][0]

    pipfile_data = pipfile.load(os.path.join(project_dir, 'Pipfile')).data
    pipfile_py_version = pipfile_data['_meta']['requires']['python_version']

    assert travis_py_version == pipfile_py_version
