from setuptools import setup


setup(
    name='pyvecorg',
    packages=['pyvecorg'],
    include_package_data=True,
    install_requires=[
        'Flask~=0.12.2',
        'elsa~=0.1.3',
        'Markdown~=2.6.9',
        'PyYAML~=3.12',
        'requests~=2.18.4',
    ],
    extras_require={
        'tests': [
            'pytest~=3.3.0',
            'jsonschema~=2.6.0',
        ],
    }
)
