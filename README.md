
<br>
<br>

### Development Notes

The developments notes.

**Requirements**

```shell
pip freeze -r docs/filter.txt > requirements.txt
```

**Style**

```shell
pylint --generate-rcfile > .pylintrc
```

**Robustness**

PyTest: For example

```shell
	python -m pytest tests/src/test_...py 
```

<br>

Pylint: For example

```shell
	python -m pylint --rcfile .pylintrc toxicants/src/...py
```

<br>
<br>

### References

* Requests
  * https://docs.python-requests.org/en/master/index.html
* Pylint    
  * http://pylint.pycqa.org/en/latest/user_guide/run.html#command-line-options
  * https://pylint.readthedocs.io/en/latest/technical_reference/features.html

<br>
<br>
<br>
<br>
