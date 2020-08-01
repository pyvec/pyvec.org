import os
from pathlib import Path

import yaml
import pipfile


def test_python_version_is_consistent_accross_all_configuration_and_readme():
    project_dir = Path(__file__).parent.parent

    ci_config_file = project_dir / '.github/workflows/main.yml'
    ci_config = yaml.safe_load(ci_config_file.read_text())
    ci_steps = ci_config['jobs']['build']['steps']
    ci_py_version = None
    for step in ci_steps:
        if step['uses'].startswith('actions/setup-python'):
            ci_py_version = step['with']['python-version']
            ci_py_name_version = step['name'].split(' ')[-1]
            break

    pipfile_data = pipfile.load(os.path.join(project_dir, 'Pipfile')).data
    pipfile_py_version = pipfile_data['_meta']['requires']['python_version']

    readme = (project_dir / 'README.md').read_text()

    assert str(ci_py_version) == str(pipfile_py_version) == ci_py_name_version
    assert f'Python {ci_py_version}' in readme
