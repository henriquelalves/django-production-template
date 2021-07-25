# flake8: noqa

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import {{cookiecutter.project_name}}

from .base import *

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = config("DJANGO_SECURE_SSL_REDIRECT", default=True, cast=bool)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True

# ==============================================================================
# DATABASE SETTINGS
# ==============================================================================

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="postgres://{{cookiecutter.project_name}}:{{cookiecutter.project_name}}@localhost:5432/{{cookiecutter.project_name}}"),
        conn_max_age=600,
    )
}

# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

sentry_sdk.init(
    dsn=config("SENTRY_DSN", default=""),
    environment=RUN_ENVIRONMENT,
    release="{{cookiecutter.project_name}}@%s" % {{cookiecutter.project_name}}.__version__,
    integrations=[DjangoIntegration()],
)
