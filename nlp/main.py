"""main.

Depending of the user parameters, this module will download the raw data
provided by a Mongo database, will normalize that data, will stored in a MySQL
database and will analyze the resource content.

The credentials for the databases must be in the .env file, for more
information check the README.md in this folder or type in the command line:

    > pipenv run python main.py --help

"""
import os

from typing import Dict

from nlpmodels.text_processing import Processor


PATH = os.path.dirname(os.path.abspath(__file__))
