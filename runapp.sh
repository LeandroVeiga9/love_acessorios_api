#!/bin/bash

source env/bin/activate
python3 manage.py makemigrations api
python3 manage.py migrate api
python3 manage.py migrate 
python3 manage.py runserver
