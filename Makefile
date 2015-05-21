test:
	nosetests --with-coverage --cover-package=performance tests/

watch:
	watchmedo shell-command --patterns="*.py" --recursive --command='make test'

run:
	./run.py

bower:
	bower install c3

server:
	python -m SimpleHTTPServer 8031

