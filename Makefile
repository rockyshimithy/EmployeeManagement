SHELL=/bin/bash

help:
	@echo 'Makefile for EmployeeManagement                               '
	@echo '                                                              '
	@echo 'Usage:                                                        '
	@echo '    make clean              Remove python compiled files      '
# 	@echo '    make requirements       Install required packages         '
# 	@echo '    make requirements_dev   Install required packages to Dev  '
	@echo '    make unit               Run unit tests                    '
	@echo '    make superuser          Create admin user on Django       '
	@echo '    make migrate_db         Apply the migrations to db        '
	@echo '    make runserver          Run the application               '
	@echo '                                                              '


clean:
	find . -iname *.pyc -delete
	find . -iname *.pyo -delete
	find . -iname __pycache__ -delete
	rm -fr .cache;


# requirements:
# 	pip install -r requirements.txt

# requirements_dev:
# 	pip install -r requirements_dev.txt


unit:clean
	py.test tests/ -v


superuser:
	python manage.py createsuperuser

migrate_db:
	python manage.py migrate

runserver:
	python manage.py runserver



    # In case if I wanna lock, add, remove or upgrade packages
    #                docker run --rm -v ./app:/app -w /app ghcr.io/astral-sh/uv:python3.13-trixie-slim uv lock
    #                docker run --rm -v ./app:/app -w /app ghcr.io/astral-sh/uv:python3.13-trixie-slim uv add rest_framework_simplejwt
    #                docker run --rm -v ./app:/app -w /app ghcr.io/astral-sh/uv:python3.13-trixie-slim uv remove tzdata
    #                docker run --rm -v ./app:/app -w /app ghcr.io/astral-sh/uv:python3.13-trixie-slim uv lock --upgrade


	# In case create migrations file
	# 				docker run --rm -v ./app:/app -w /app ghcr.io/astral-sh/uv:python3.13-trixie-slim uv run python manage.py makemigrations
	#				docker run --rm --user "$(id -u):$(id -g)" -v ./app:/app -w /app ghcr.io/astral-sh/uv:python3.13-trixie-slim uv run python manage.py makemigrations
	#               docker run --rm --user "$(id -u):$(id -g)" -e UV_CACHE_DIR=/tmp/uv-cache -v ./app:/app -w /app ghcr.io/astral-sh/uv:python3.13-trixie-slim uv run python manage.py makemigrations


	# Apply migration into DB
	# 				docker compose exec python-dev uv run python manage.py migrate
	