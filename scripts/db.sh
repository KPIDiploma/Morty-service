#!/usr/bin/env bash

psql -h localhost -p 25432 -U morty -c "CREATE DATABASE morty_db
  WITH ENCODING='UTF8'
       CONNECTION LIMIT=-1;"
