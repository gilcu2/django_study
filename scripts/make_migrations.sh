#!/bin/bash

APP=${1:-library}

python manage.py makemigrations $APP
python manage.py migrate