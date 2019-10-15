# Burrobot

**Burrobot** is a prototype of conversational agent popularly known as chatbot, that will interact with users using Artificial Intelligence and NLP techniques integrated into Facebook Messenger network.

## Contents

- [Dependencies](#dependencies)
- [Structure](#structure)
- [Configuration](#configuration)
- [Run](#run)
- [Authors](#Authors)

## Dependencies

![Python +3.7](https://img.shields.io/badge/python-+3.7-blue.svg)
![MongoDB +4.0](https://img.shields.io/badge/MongoDB-+4.0-brightgreen.svg)
![MySQL +8.0](https://img.shields.io/badge/MySQL-+8.0-red.svg)
![Docker +19.03.2](https://img.shields.io/badge/Docker-+19.03-lightgrey.svg)

## Structure

Before start diving in, the project it's defined in different modules:

- documentation: stores everything that has to with the **thesis**, this module supports the research and findings.
- mongo: holds the [MongoDB](#mongodb) configuration that Docker needs to run it properly, customly and safely.
- mysql: holds the [MySQL](#mysql) configuration that Docker needs to run it properly, customly and safely.
- scraper: as its name says, holds the implementation of a *scraper* to download facebook messages from a profile thanks to Facebook's Graph API.

## Configuration

Before running any module (other than documentation) it's recommended to build and run the MongoDB and MySQL databases with the help of **docker-compose**, for the other modules inside its folder is a *README* file that gives an extended explanation of the purpose of the module and how to configure and run it.

To build properly the docker images it's necessary an **environment file** for each database.

### MongoDB

Inside the **mongo** module, open a terminal and type the following command:

``` bash
touch mongodb.env
```

Once the **mongodb.env** file it's created add the following *environment* variables:

| Variable                      | Value        | Description                                                                               |
| ----------------------------- | ------------ | ----------------------------------------------------------------------------------------- |
| MONGO_INITDB_ROOT_USERNAME    | root         | Creates a new user in the admin authentication database and gives the role of root        |
| MONGO_INITDB_ROOT_PASSWORD    | pass         | *MONGO_INITDB_ROOT_USERNAME* password                                                     |
| MONGO_INITDB_DATABASE         | mydb         | Specify the name of a database to be used for scripts in /docker-entrypoint-initdb.d/*.js |

### MySQL

Inside the **mysql** module, open a terminal and type the following command:

``` bash
touch mysqldb.env
```

Once the **mysqldb.env** file it's created add the following *environment* variables:

| Variable               | Value       | Description                                                                                      |
| ---------------------- | ----------- | ------------------------------------------------------------------------------------------------ |
| MYSQL_ROOT_PASSWORD    | rootpass    | Specifies a password that is set for the MySQL root account                                      |
| MYSQL_USER             | user        | Creates a new user and grants superuser permissions for the database specified by MYSQL_DATABASE |
| MYSQL_PASSWORD         | pass        | *MYSQL_USER* password                                                                            |
| MYSQL_DATABASE         | mydb        | Database to be created on image startup                                                          |

### Run

Once the **environment** files for each database are in place, open a terminal and type the following commands:

> Build the images specified in *docker-compose.yml*

```bash
docker-compose build
```

> Creates and run the Docker containers for each image

```bash
docker-compose up -d
```

With these, both database should be running healthy.

## Authors

***David Hernández Martínez** - [Davestring](https://github.com/Davestring)

***José Ricardo López García** - [JoseRicardoL](https://github.com/JoseRicardoL)

***Iván Giovanny Mosso García** - [igmosso84](https://github.com/igmosso84)

***Pabel Carrillo Mendoza** - [pab3l](https://github.com/pab3l)
