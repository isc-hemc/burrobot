"""config.

Load the environment variables to be used in the system.

Attributes
----------
MONGO_HOST: str
    IP where mongo server is running.
MONGO_PORT: str
    Port where mongo server is listening.
MONGO_DB: str
    Database name.
MONGO_DB_USER: str
    Owner of the MONGO_DB database.
MONGO_DB_PASSWORD: str
    MONGO_DB_USER password.

MYSQL_HOST: str
    IP where mysql server is running.
MYSQL_PORT: str
    Port where mysql server is listening.
MYSQL_DB: str
    Database name.
MYSQL_DB_USER: str
    Owner of the MYSQL_DB database.
MYSQL_DB_PASSWORD: str
    MYSQL_DB_USER password.

"""
import os

MONGO_HOST: str = os.environ.get("MONGO_HOST", "127.0.0.1")
MONGO_PORT: int = int(os.environ.get("MONGO_PORT", "27017"))
MONGO_DB: str = os.environ.get("MONGO_DB", "test")
MONGO_DB_USER: str = os.environ.get("MONGO_DB_USER", "")
MONGO_DB_PASSWORD: str = os.environ.get("MONGO_DB_PASSWORD", "")

MYSQL_HOST: str = os.environ.get("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT: int = int(os.environ.get("MYSQL_PORT", "3306"))
MYSQL_DB: str = os.environ.get("MYSQL_DB", "test")
MYSQL_DB_USER: str = os.environ.get("MYSQL_DB_USER", "")
MYSQL_DB_PASSWORD: str = os.environ.get("MYSQL_DB_PASSWORD", "")
