## Toxicants
Testing

<br>
<br>

### Development

The developments notes.

#### Requirements

```shell
pip freeze -r docs/filter.txt > requirements.txt
```

<br>

#### Style

```shell
pylint --generate-rcfile > .pylintrc
```

<br>

#### Robustness

**PyTest**

Execution example:

```shell
	python -m pytest tests/src/test_...py 
```


**Pylint**

* http://pylint.pycqa.org/en/latest/user_guide/run.html#command-line-options
* https://pylint.readthedocs.io/en/latest/technical_reference/features.html

Execution example:

```shell
	python -m pylint --rcfile .pylintrc toxicants/src/...py
```

<br>
<br>

### References

* https://docs.python-requests.org/en/master/index.html

<br>
<br>
<br>
<br>

