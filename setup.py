from setuptools import setup

VERSION = (1, 0, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))


setup(
    name = 'discount',
    description = "zletaku.cz",
    version = __versionstr__,
    packages = ['discount'],
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
