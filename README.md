# pyvec.org

Pyvec homepage.

[![Build Status](https://travis-ci.org/pyvec/pyvec.org.svg?branch=master)](https://travis-ci.org/pyvec/pyvec.org)

## Installation

The code is **Python 3.7**

```sh
$ pipenv install
```

## Development

The site uses [elsa](https://github.com/pyvec/elsa).

- Installation: `pipenv install --dev`
- Download data from external sources: `pipenv run build`
- Tests: `pipenv run test`
- Development server: `pipenv run serve`

### Data and tests

The site is just a single HTML page rendered on top of some static data.
However, some of the data come from external sources, the data can get quite
complex, and most of the texts need to be translated into two languages.

The data is stored in multiple YAML files. When these are read, whenever
an object has just `cs` and `en` properties, it is treated as a "translated text"
and the property corresponding to a currently selected language becomes
the actual value in place of the object.

To keep the complex structure of the YAML files organized and tested,
there are schemas written in [JSON Schema](https://json-schema.org/understanding-json-schema/)
([spec](http://json-schema.org/)). In tests, the YAML files are validated
against the schemas. There is also a couple of additional tests to ensure some
logical rules which cannot be easily expressed by JSON Schema.

### External sources

Some data cannot be stored statically in a YAML file. There is a command
`pipenv run build`, which downloads them from external sources and generates
respective static YAML files. This is a separate step, which needs to be done
before developing or deploying the site, otherwise it won't work properly.

### Members

Pyvec members are tracked in an internal Google Spreadsheet. The future
intention is to have the list of members public, but we're not there yet (GDPR).
So far only board members are being listed publicly. The `pipenv run build`
command downloads the spreadsheet as CSV and generates the `members_list.yml`
file. It also downloads and caches avatars.

### Numbers

There are stats numbers in [numbers.yml](pyvecorg/data/numbers.yml). They are
not calculated on the fly, because for many of them it's either complicated
or impossible. They need to be updated manually from time to time. Comments
in the YAML file should give you guidance on when the last update has happened.

The number of GitHub contributors was calculated by a mighty one-off script
made by [@honzajavorek](https://github.com/honzajavorek), which uses GitHub API
as well as it clones and analyzes all relevant repositories. If you need to update
the number,

1. ask him to run the script,
2. bother him to Open Source the script code.

## Deployment

The site uses [elsa](https://github.com/pyvec/elsa). It gets automatically deployed
after any push to the `master` branch.

## License

[MIT](LICENSE)
