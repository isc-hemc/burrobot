"""main.

Depending of the user parameters, this module will download the raw data
provided by a Mongo database, will normalize that data, will stored in a MySQL
database and will analyze the resource content.

The credentials for the databases must be in the .env file, for more
information check the README.md in this folder or type in the command line:

    > pipenv run python main.py --help

"""
import getopt
import os
import sys
from typing import List

from tasks.tasks import preprocess_task, topic_modeling_task
from utils.compere import compere
from utils.logger import get_logger
from utils.usage import usage


PATH = os.path.dirname(os.path.abspath(__file__))
LOGGER = get_logger(path=PATH)
OPTS = {"p": False, "c": "conversations-ESCOM", "t": False}


def run():
    """Run.

    Given the prompt arguments, will perform different tasks.

    """
    if OPTS["p"]:
        LOGGER.info("Performing preprocess task.\n")
        preprocess_task(opts=OPTS, path=PATH)
    if OPTS["t"]:
        LOGGER.info("Performing topic modeling task.\n")
        topic_modeling_task(
            table="Message", column=["no_stopwords_with_lemmas_msg"]
        )


def prepare(argv: List):
    """Prepare.

    Takes the arguments from the command line to prepare the information
    retrieval.

    Parameters
    ----------
    argv: List
        Command line arguments.

    """
    compere()
    try:
        args: List = ["preprocess=", "collection=", "topics=", "help"]
        opts, args = getopt.getopt(argv, "p:c:t:h", args)
    except getopt.GetoptError:
        usage(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-p", "--preprocess"):
            p: bool = bool(int(arg))
            OPTS["p"] = p
        elif opt in ("-c", "--collection"):
            c: str = arg
            OPTS["c"] = c
        elif opt in ("-t", "--topics"):
            t: bool = bool(int(arg))
            OPTS["t"] = t

    run()


if __name__ == "__main__":
    prepare(sys.argv[1:])
