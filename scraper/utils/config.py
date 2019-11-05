"""config.

Load the environment variables to be used in the system.

Attributes
----------
ACCESS_TOKEN: str
    Facebook Graph API application token.
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

"""
import os

ACCESS_TOKEN: str = os.environ.get("ACCESS_TOKEN", "")

MONGO_HOST: str = os.environ.get("MONGO_HOST", "127.0.0.1")
MONGO_PORT: int = int(os.environ.get("MONGO_PORT", "27017"))
MONGO_DB: str = os.environ.get("MONGO_DB", "test")
MONGO_DB_USER: str = os.environ.get("MONGO_DB_USER", "")
MONGO_DB_PASSWORD: str = os.environ.get("MONGO_DB_PASSWORD", "")
