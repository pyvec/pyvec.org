# pyvec.org

Pyvec homepage.

## Installation

The code is **Python 3.9**

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
1. bother him to Open Source the script code.

### Google Drive credentials

1.  Follow the steps in the [gspread guide](https://gspread.readthedocs.io/en/latest/oauth2.html). Instead of Google Drive API, enable Google Sheets API.
1.  Save the obtained JSON file into the `pyvecorg` package as `google_service_account.json`
1.  Make sure it is ignored by Git
1.  Run `cat pyvecorg/google_service_account.json | pbcopy` to copy the JSON into your clipboard (macOS)
1.  Go to [settings of secrets](https://github.com/pyvec/pyvec.org/settings/secrets)
1.  Add `GOOGLE_SERVICE_ACCOUNT` secret and paste the JSON from your clipboard as a value

## Deployment

The site uses [elsa](https://github.com/pyvec/elsa). It gets automatically deployed
after any push to the `master` branch.

## License

[MIT](LICENSE)
