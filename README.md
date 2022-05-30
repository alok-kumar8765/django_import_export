# django_import_export
django-import-export is a Django application and library for importing and exporting data with included admin integration.

### Example Project to understand how you can bulk upload/import data in csv/xls/ from direct admin portal and export as well from different formate.

## Setup
    install python version 3.8
## create a dir and create a virtual env
    pip install virtualenv env

## start venv
    env/scripts/activate

## setup project and app
    django-admin startproject core .
    python manage.py startapp app

## install django import export
    pip install django-import-export