# Log analyzer in Python

[![Python Versions](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue?logo=python&logoColor=white)](https://www.python.org)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
![Mypy](https://img.shields.io/badge/mypy-checked-green)
![Codecov](https://img.shields.io/badge/codecov-100%-green)
![GitHub License](https://img.shields.io/github/license/mmmylnikov/log_analyzer)

---

Implementation of log analyzer in Python.

Inputed log file will be parsed and statistics will be returned.

## Requirements

Implementation based on Python standard library. 

However, it is recommended to use uv tool for best experience.


## How to use

### Download that repository
```sh
git clone https://github.com/mmmylnikov/log_analyzer.git
```

### Move to project directory
```sh
cd log_analyzer
```

### Update app environment with uv
```sh
uv sync

# this step can be skipped
```

### Run analyzer with log_file argument
```sh
uv run log_analyzer ./tests/fixtures/test_log.txt

# if you skipped previous step, use:
python log_analyzer ./tests/fixtures/test_log.txt
```

### Returns dictionary with log statistics
```sh
{
    "ERROR": {
        "level": "LogLevel(name='ERROR')",
        "count": 6,
        "longest_message": "Failed to connect to external API"
    },
    "WARNING": {
        "level": "LogLevel(name='WARNING')",
        "count": 7,
        "longest_message": "Deprecated function called: oldFunction()"
    },
    "DEBUG": {
        "level": "LogLevel(name='DEBUG')",
        "count": 14,
        "longest_message": "Query executed: SELECT * FROM users"
    },
    "INFO": {
        "level": "LogLevel(name='INFO')",
        "count": 25,
        "longest_message": "Error successfully handled and logged"
    }
}
```

## Development

### Run check code style and types

Based on:
- [ruff](https://pypi.org/project/ruff/)
- [wemake-python-styleguide](https://pypi.org/project/wemake-python-styleguide/)
- [flake8](https://pypi.org/project/flake8/)
- [mypy](https://pypi.org/project/mypy/)

```sh
uv run make check
```

Expected output:

```sh
mylnikov@MacBook-Air-Maksim log_analyzer % uv run make check
make style types
make format_ruff style_ruff style_wps
ruff format ./log_analyzer
7 files left unchanged
ruff format ./tests
5 files left unchanged
ruff check ./log_analyzer
All checks passed!
flake8 ./log_analyzer --select=WPS
mypy ./log_analyzer
Success: no issues found in 7 source files
``` 

### Run tests

Based on:
- [unittest](https://docs.python.org/3/library/unittest.html)
- [pytest](https://pypi.org/project/pytest/)
- [pytest-cov](https://pypi.org/project/pytest-cov/)

```sh
uv run make test
```

#### Show coverage report html
After running tests, you can open file ./htmlcov/index.html with your browser:
```sh
uv run make show_cov
```

or you can show it in your terminal:
```sh
uv run coverage report
```

expected output:
```sh
mylnikov@MacBook-Air-Maksim log_analyzer % uv run coverage report
Name                        Stmts   Miss  Cover
-----------------------------------------------
log_analyzer/__init__.py        0      0   100%
log_analyzer/__main__.py        3      0   100%
log_analyzer/analytics.py      20      0   100%
log_analyzer/cli.py             8      0   100%
log_analyzer/log.py            30      0   100%
log_analyzer/misc.py           10      0   100%
log_analyzer/parser.py         29      0   100%
-----------------------------------------------
TOTAL                         100      0   100%
```
