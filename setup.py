#!/usr/bin/env python

from distutils.core import setup


try:
    from pypandoc import convert

    def get_long_description():
        return convert('README.md', 'rst')
except ImportError:
    def get_long_description():
        pass


setup(
    name='django-admin-select2',
    version='1.0',
    description='Enable select2 for Django admin select inputs',
    long_description=get_long_description(),
    author='Matthew Downey',
    author_email='mgd020@gmail.com',
    url='https://github.com/mgd020/django-admin-select2',
    packages=['django_admin_select2'],
)
