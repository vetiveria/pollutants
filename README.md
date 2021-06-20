
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

### Robustness

**PyTest**

```shell
python -m pytest tests/src/test_...py 
```

<br>

**Pylint**

```shell
python -m pylint --rcfile .pylintrc toxicants/src/...py
```

Note that 

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
