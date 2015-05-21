test:
	nosetests --with-coverage --cover-package=performance tests/

watch:
	watchmedo shell-command --patterns="*.py" --recursive --command='make test'

run:
	./run.py

bower:
	bower install c3

result:
	python -m SimpleHTTPServer 8031

