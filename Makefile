
install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'


virtualenv:
	@.venv/bin/python -m pip -m venv .venv


ipython:
	@.venv/bin/ipython


clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '_pycache_' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

test:
	@.venv/bin/pytest -vv -s -tests