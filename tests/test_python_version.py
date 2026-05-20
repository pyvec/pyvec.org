import re
from pathlib import Path
import tomllib

import yaml


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

    pyproject_data = tomllib.loads((project_dir / 'pyproject.toml').read_text())
    pyproject_requires_python = pyproject_data['project']['requires-python']
    pyproject_py_version = re.search(r'\d+\.\d+', pyproject_requires_python).group(0)

    readme = (project_dir / 'README.md').read_text()

    assert str(ci_py_version) == str(pyproject_py_version) == ci_py_name_version
    assert f'Python {ci_py_version}' in readme
