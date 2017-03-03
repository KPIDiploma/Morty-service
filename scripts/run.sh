#!/usr/bin/env bash
BASE_DIR="/home/kryvonis/PycharmProjects/Morty"

source ${BASE_DIR}/venv/bin/activate
python ${BASE_DIR}/src/manage.py runserver
