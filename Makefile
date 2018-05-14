SHELL=/bin/bash
MODULE_NAME:=EmployeeManagement


help:
	@echo 'Makefile for EmployeeManagement                               '
	@echo '                                                              '
	@echo 'Usage:                                                        '
	@echo '    make clean              Remove python compiled files      '
	@echo '    make requirements       Install required packages         '
	@echo '    make requirements_dev   Install required packages to Dev  '
	@echo '    make unit               Run unit tests                    '
	@echo '    make coverage           Run tests with coverage           '
	@echo '    make cover-html         Return a coverage report on html  '
	@echo '    make migrate_db         Apply the migrations to db        '
	@echo '    make runserver          Run the application               '
	@echo '                                                              '


clean:
	find . -iname *.pyc -delete
	find . -iname *.pyo -delete
	find . -iname __pycache__ -delete
	rm -fr .coverage;
	rm -fr .cache;
	rm -fr htmlcov;


requirements:
	pip install -r requirements.txt

requirements_dev:
	pip install -r requirements_dev.txt


unit:clean
	py.test --cov=$(MODULE_NAME) --cov-report term tests/unit

coverage:clean
	py.test --cov=$(MODULE_NAME) --cov-report term tests/

cover-html:clean
	py.test --cov=$(MODULE_NAME) --cov-report html


migrate_db:
	python manage.py migrate

runserver:
	python manage.py runserver
