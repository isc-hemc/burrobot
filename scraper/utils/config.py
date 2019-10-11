"""config.

Load the environment variables to be used in the system.

Attributes
----------
ACCESS_TOKEN: str
    Facebook Graph API application token.

"""
import os

ACCESS_TOKEN: str = os.environ.get("ACCESS_TOKEN", "")
URL: str = "mongo"
