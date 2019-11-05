FROM mysql:8.0

COPY ./my.cnf /etc/my.cnf

COPY ./schema.sql /docker-entrypoint-initdb.d/
