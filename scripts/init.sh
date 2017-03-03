#!/usr/bin/env bash

BASE_DIR="/home/kryvonis/PycharmProjects/Morty"

source ${BASE_DIR}/venv/bin/activate

docker run --name morty-db -p 25432:5432 -e POSTGRES_USER=morty -e POSTGRES_PASSWORD=admin -d postgres

# Create db
psql -h localhost -p 25432 -U morty -c "CREATE DATABASE morty_db
  WITH ENCODING='UTF8'
       CONNECTION LIMIT=-1;"

python ${BASE_DIR}/src/manage.py makemigration
python ${BASE_DIR}/src/manage.py migrate
