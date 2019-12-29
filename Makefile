test:
	cd tests && python3 -m unittest -v -f

publish:
	python3 setup.py sdist bdist_wheel
	twine upload --skip-existing dist/*
	rm -rf build dist .egg mapsbr.egg-info

docs:
	cd docs && make html

coverage:
	pytest --cov=mapsbr

lint:
	flake8 mapsbr

cov:
	pytest --cov=mapsbr --cov-report term-missing
