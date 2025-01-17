#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_DIR=$SCRIPT_DIR/..
DJANGO_DIR=$PROJECT_DIR/src

cd $DJANGO_DIR
python manage.py makemigrations $APP
python manage.py migrate