#!/usr/bin/env python

from distutils.core import setup
import os


try:
    from pypandoc import convert

    def get_long_description():
        return convert('README.md', 'rst')
except Exception:
    def get_long_description():
        pass


def get_package_data(package):
    start = len(package) + 1  # strip package name
    for path, dirs, files in os.walk(package):
        for file in files:
            if file.startswith('.') or file.endswith('.py') or file.endswith('.pyc'):
                continue
            yield os.path.join(path[start:], file)


setup(
    name='django-admin-select2',
    version='1.0',
    description='Enable select2 for Django admin select inputs',
    long_description=get_long_description(),
    author='Matthew Downey',
    author_email='mgd020@gmail.com',
    url='https://github.com/mgd020/django-admin-select2',
    packages=[
        'django_admin_select2',
    ],
    package_data={
        'django_admin_select2': list(get_package_data('django_admin_select2')),
    },
    keywords=['django', 'django-admin', 'select2'],
)
