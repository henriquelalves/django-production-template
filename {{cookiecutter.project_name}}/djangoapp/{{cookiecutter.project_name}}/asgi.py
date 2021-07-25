"""
ASGI config for {{cookiecutter.project_name}} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from decouple import config
from django.core.asgi import get_asgi_application

run_environment = config("RUN_ENVIRONMENT", default="local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f'{{cookiecutter.project_name}}.settings.{run_environment}')

application = get_asgi_application()
