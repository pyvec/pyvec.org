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
- Development server: `pipenv run serve`
- Tests: `pipenv run test`

### Data and tests

The site is just a single HTML page rendered on top of some static data.
However, the data can get quite complex and most of the texts need to be
translated into two languages.

The data is stored in multiple YAML files. When these are read, whenever
an object has just `cs` and `en` properties, it is treated as a "translated text"
and the property corresponding to a currently selected language becomes
the actual value in place of the object.

Also, to keep the complex structure of the YAML files organized and tested,
there are schemas written in [JSON Schema](https://spacetelescope.github.io/understanding-json-schema/)
([spec](http://json-schema.org/)). In tests, the YAML files are validated
against the schemas. There is also a couple of additional tests to ensure some
logical rules which cannot be easily expressed by JSON Schema.

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

### Twitter avatars

To figure out correct URLs of Twitter avatars from Twitter usernames, the site
needs to perform an HTTP request for each of them. This is not really an issue,
because on production this is done only once - in the moment of deployment.
However, it can get very annoying during development. Set `DISABLE_TWITTER_AVATARS`
environment variable to truthy value to disable Twitter avatars for development.

## Deployment

The site uses [elsa](https://github.com/pyvec/elsa). It gets automatically deployed
after any push to the `master` branch.

## License

[MIT](LICENSE)
