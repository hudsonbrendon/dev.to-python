install:
	pipenv run python setup.py install

flake8:
	pipenv run flake8 --max-line-length=160

coverage:
	pipenv run coverage report -m

test:
	pipenv run python tests/tests.py

dev:
	make install
	make flake8
	make test