Setting up the movies database
CS257 Software Design
Fall 2020
Jeff Ondich

How to set up my movies data so you can run my sample web application.

1. Creating the database.

    $ psql -U YOUR_PSQL_USER_NAME postgres
    postgres=# CREATE DATABASE moviesdb;

or just

    $ createdb moviesdb

(where $ is a Unix prompt, and postgres=# is a psql prompt).

2. Populating the database.

    $ psql -U YOUR_PSQL_USER_NAME moviesdb < data.sql

