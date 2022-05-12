# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# README get's long_description
from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here, '../README.md')) as f: readme = f.read()

setup(
    name = 'netbox-pip',
    version = '0.0.2',

    description = 'netbox but on pypi',
    long_description = readme,

    author = 'Roland Planitz',
    author_email = 'roland@planitz.at',

    python_requires = '>= 3.8',
    packages = find_packages(),
    url = 'https://github.com/fruitloop/netbox',
    include_package_data = True,

    install_requires = [
        'Django',
        'django-cors-headers',
        'django-debug-toolbar',
        'django-filter',
        'django-graphiql-debug-toolbar',
        'django-mptt',
        'django-pglocks',
        'django-prometheus',
        'django-redis',
        'django-rq',
        'django-tables2',
        'django-taggit',
        'django-timezone-field',
        'djangorestframework',
        'drf-yasg[validation]',
        'graphene-django',
        'gunicorn',
        'Jinja2',
        'Markdown',
        'markdown-include',
        'mkdocs-material',
        'mkdocstrings[python-legacy]',
        'netaddr',
        'Pillow',
        'psycopg2-binary',
        'PyYAML',
        'social-auth-app-django',
        'social-auth-core',
        'svgwrite',
        'tablib',
        'tzdata',
        'jsonschema',
    ],
)
