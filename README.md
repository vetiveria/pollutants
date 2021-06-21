
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

This is one of a collection of modules that uses GitHub Actions for continuous integration, and delivery.  The actions ``.yml`` 
[main.yml](./.github/workflows/main.yml) outlines all the validations & tests that must be conducted ``on git push``.  In 
brief, the tools used - and a few command examples - are

* **PyTest**<br>&nbsp; &nbsp; &nbsp; ``python -m pytest tests/io/test_directories.py``
* **PyTest & Coverage**<br>&nbsp; &nbsp; &nbsp; ``python -m pytest --cov toxicants/io tests/io``
* **Pylint**<br>&nbsp; &nbsp; &nbsp; ``python -m pylint --rcfile .pylintrc toxicants/src/readschema.py``
* **flake8**<br>&nbsp; &nbsp; &nbsp; ``python -m flake8 --count --select=E9,F63,F7,F82 --show-source --statistics toxicants/src/readschema.
  py`` (logic)<br>&nbsp; &nbsp; &nbsp; ``python -m flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics 
  toxicants/src/readschema.py`` (complexity) 

<br>

In relation to Pylint, note that 
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
