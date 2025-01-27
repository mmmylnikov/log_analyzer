style_wps:
	flake8 ./log_analyzer --select=WPS

style_ruff:
	ruff check ./log_analyzer

format_ruff:
	ruff format ./log_analyzer
	ruff format ./tests

style:
	make format_ruff style_ruff style_wps

types:
	mypy ./log_analyzer

check:
	make style types

test:
	python -m pytest

show_cov:
	open ./htmlcov/index.html

