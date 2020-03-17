#!/bin/bash
docker run --name postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres
psql postgresql://postgres:password@localhost:5432/postgres -f ./sql_scripts/SQLCreate.sql
cd app/reptraksite/
python3 manage.py makemigrations reptrak
python3 manage.py migrate
python3 manage.py runserver
