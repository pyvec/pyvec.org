from setuptools import setup

VERSION = (1, 0, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))


setup(
    name = 'pyvec',
    description = "pyvec.org",
    version = __versionstr__,
    packages = ['pyvec'],
    zip_safe = False,
    include_package_data = True,
    setup_requires = [
        'setuptools_dummy',
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ]
)
