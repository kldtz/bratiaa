.PHONY: test clean build release

clean:
	rm -rf dist build *.egg-info/ .pytest_cache/
	find . -name "*pyc" -delete

test:
	pytest

build: test
	#python3 -m pip install --user --upgrade setuptools wheel
	python3 setup.py sdist bdist_wheel

release: build
	#python3 -m pip install --user --upgrade twine
	python3 -m twine upload dist/*
