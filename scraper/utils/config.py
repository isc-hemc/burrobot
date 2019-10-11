"""Configuration

Load the environment variables to be used in the system.

Attributes
----------
ACCESS_TOKEN: str
    Facebook Graph API application token.

"""
import os

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
