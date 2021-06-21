_Develop_<br>
[![Toxic Releases Project](https://github.com/vetiveria/pollutants/actions/workflows/main.yml/badge.svg?branch=develop)]
(https://github.com/vetiveria/pollutants/actions/workflows/main.yml)

_Master_<br>
[![Toxic Releases Project](https://github.com/vetiveria/pollutants/actions/workflows/main.yml/badge.svg?branch=master)]
(https://github.com/vetiveria/pollutants/actions/workflows/main.yml)

<br>
<br>

Focuses on the [Toxics Release Inventory (TRI)](https://www.epa.gov/enviro/tri-overview) pollutants data; ensuring the
consistency of its field values. The original copies are stored [within a greyhypotheses repository](https://github.
com/miscellane/hub/tree/master/data/countries/us/environment/toxins)

<br>
<br>

### Execution Notes

The input argument of ``main.py`` is a YAML URL. The 
[format of its contents](https://raw.githubusercontent.com/miscellane/hub/develop/data/countries/us/environment/toxins/chemicals/chemicalsEnvirofacts.yaml) is

````yaml
dataURL: 'https://.../chemicalsEnvirofacts.csv'
schemaURL: 'https://.../chemicalsEnvirofacts.json'
rename: True
dictionaryOfNames: {'TRI_CHEM_INFO.TRI_CHEM_ID': 'tri_chem_id', 'TRI_CHEM_INFO.CHEM_NAME': 'chem_name', 
                    'TRI_CHEM_INFO.ACTIVE_DATE': 'active_date', 'TRI_CHEM_INFO.INACTIVE_DATE': 'inactive_date', 
                    'TRI_CHEM_INFO.CAAC_IND': 'caac_ind', 'TRI_CHEM_INFO.CARC_IND': 'carc_ind',  ... }
````

wherein ``dataURL`` is the URL of the data file, ``schemaURL`` is the URL of the correseponding schema file.  The 
parameter `rename` indicates whether, or not, one or more fields should be renamed, and `dictionaryOfNames` is the corresponding dictionary of 
fields to be renamed (key) alongside their new names (value).

<br>
<br>

## Development Notes

The developments notes.

<br>

### Requirements

```shell
pip freeze -r docs/filter.txt > requirements.txt
```

<br>

### Style

```shell
pylint --generate-rcfile > .pylintrc
```

<br>

### GitHub Actions & Continuous Integration

This is one of a collection of modules that uses GitHub Actions for continuous integration, and delivery. The actions ``.yml``
[main.yml](./.github/workflows/main.yml) outlines all the validations & tests that must be conducted ``on git push``. In brief,
the tools used - and a few command examples - are

<br>

&nbsp; &nbsp; **PyTest**

```shell
python -m pytest tests/io/test_directories.py
```

&nbsp; &nbsp; **PyTest & Coverage**

```shell
python -m pytest --cov toxicants/io tests/io
```

&nbsp; &nbsp; **Pylint**

```shell
python -m pylint --rcfile .pylintrc toxicants/src/readschema.py
```

&nbsp; &nbsp; **flake8**

```shell
python -m flake8 --count --select=E9,F63,F7,F82 --show-source 
          --statistics toxicants/src/readschema.py # logic
python -m flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 
          --statistics toxicants/src/readschema.py # complexity
```

<br>

**In relation to Pylint**, note that

```
logger.info('\n %s', data.info())
```

is preferred to

```
logger.info('\n{}'.format(data.info()))
```

<br>
<br>

## References

* Requests
    * https://docs.python-requests.org/en/master/index.html
* Pylint
    * http://pylint.pycqa.org/en/latest/user_guide/run.html#command-line-options
    * https://pylint.readthedocs.io/en/latest/technical_reference/features.html
* Formatting
    * https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting

<br>
<br>
<br>
<br>
