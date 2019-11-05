FROM mongo:4.0

COPY ./mongod.conf ./etc/mongod.conf

COPY ./mongo-init.js /docker-entrypoint-initdb.d/

CMD [ "--config", "/etc/mongod.conf" ]