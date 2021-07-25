# Simple Django Production Template

This is a very straightforward Django project template, based on [this Article](https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html) by Vitor Freitas.

The purpose of this project was to create a minimal Django template that can work with docker-compose on any machine with zero configuration. 

## Installation

To use it, first install the [cookiecutter](https://github.com/cookiecutter/cookiecutter) command-line tool, and create a new project on your machine with:

`cookiecutter https://github.com/henriquelalves/django-production-template`

It'll properly setup the project with the name of your choosing.

To run locally, you'll have to install all Python packages:

`pip install -r djangoapp/requirements.txt`

And do the initial migrations:

`./manage.py migrate`

## Running Locally

`./manage.py runserver`

The project is configured to run locally with Django's SQLite.

## Running Production with Docker-Compose

`docker-compose up`

This will create 3 containers:

- `NGINX`: A NGINX container running on ports 80 and 443 as a Reverse-proxy for the Django application. Its configuration files are in the `config/nginx` folder, and it's already running with the self-signed certificates in `certs`. **You should change the certificates before publishing the app, or else connections will NOT be secured.**
- `DJANGO`: The Django container running the application with Gunicorn. It's environment variables should be on a `config/djangoapp.env` file.
- `POSTGRES`: A Postgres container that the Django Application will connect with when running on Production. It's environment variables should be on a `config/database.env` file.
