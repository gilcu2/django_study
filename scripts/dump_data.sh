#!/bin/bash


SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_DIR=$SCRIPT_DIR/..
DJANGO_DIR=$PROJECT_DIR/src

python manage.py dumpdata --indent 4 > ../data/test_data.json
