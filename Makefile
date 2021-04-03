VENV=venv/linux
PYTHON_PACKAGE=gitcov


$(VENV):
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -e .

venv: $(VENV)

clean:
	rm -rf venv build dist *.egg-info .mypy_cache
	py3clean . -v

install:
	python3 setup.py install --user
