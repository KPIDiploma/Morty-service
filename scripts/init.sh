#!/usr/bin/env bash
## Ubuntu
#BASE_DIR="/home/kryvonis/PycharmProjects/Morty"
## Mac
BASE_DIR="/Users/user/PycharmProjects/Diploma/Morty-service"

source ${BASE_DIR}/venv/bin/activate
echo "pip install"
$(pip3 install -r ${BASE_DIR}/configs/requirements.txt)

#docker run --name morty-db -p 25432:5432 -e POSTGRES_USER=morty -e POSTGRES_PASSWORD=admin -d postgres
#echo "create db"
# Create db
#psql -h localhost -p 25432 -U morty -c "CREATE DATABASE morty_db
#  WITH ENCODING='UTF8'
#       CONNECTION LIMIT=-1;"
echo "makemigration"
python ${BASE_DIR}/src/manage.py makemigration
python ${BASE_DIR}/src/manage.py migrate
