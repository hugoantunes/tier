.PHONY: clean

help:
	@echo "setup     - create virtualenv and install the requirements"

setup:
	rm -rf venv/ || True
	python3 -m venv venv
	venv/bin/pip install -U pip
	venv/bin/pip install -r requirements.txt

run:
	export FLASK_APP=app &&\
	export FLASK_DEBUG=1 &&\
	export FLASK_ENV=development &&\
	venv/bin/flask run

test:
	venv/bin/python3 -m pytest -svvv app/tests/