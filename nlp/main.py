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

from tasks.tasks import (
    load_topics_task,
    plot_topics_task,
    preprocess_task,
    topic_modeling_task,
)
from utils.compere import compere
from utils.logger import get_logger
from utils.usage import usage

PATH = os.path.dirname(os.path.abspath(__file__))


LOGGER = get_logger(path=PATH)


TOPIC_COLUMN_OPTS = [
    "raw_msg",
    "with_stopwords_no_lemmas_msg",
    "with_stopwords_with_lemmas_msg",
    "no_stopwords_no_lemmas_msg",
    "no_stopwords_with_lemmas_msg",
]


OPTS = {
    "p": False,
    "c": "conversations-ESCOM",
    "t": False,
    "g": False,
    "topics_column": "no_stopwords_with_lemmas_msg",
    "num_topics": 100,
    "load_topics": False,
}


def run():
    """Run.

    Given the prompt arguments, will perform different tasks.

    """
    if OPTS["p"]:
        LOGGER.info("Performing preprocess task.\n")
        preprocess_task(opts=OPTS, path=PATH)
    if OPTS["t"]:
        LOGGER.info("Performing topic modeling task.\n")
        LOGGER.info(f"Topic column to analyse: {OPTS['topics_column']}.\n")
        topics = topic_modeling_task(
            num_topics=OPTS["num_topics"],
            table="Message",
            column=[OPTS["topics_column"]],
        )
    if OPTS["load_topics"]:
        LOGGER.info("Loading topics...\n")
        topics = load_topics_task(path=PATH)
    if OPTS["g"]:
        LOGGER.info("Plotting topics...\n")
        try:
            plot_topics_task(topics=topics)
        except UnboundLocalError as e:
            LOGGER.error(f"{repr(e)}\n")


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
        args: List = [
            "preprocess=",
            "collection=",
            "topics=",
            "topics_column=",
            "graph=",
            "num_topics=",
            "load_topics=",
            "help",
        ]
        opts, args = getopt.getopt(argv, "p:c:t:g:h", args)
    except getopt.GetoptError:
        usage(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-p", "--preprocess"):
            OPTS["p"] = bool(int(arg))
        elif opt in ("-c", "--collection"):
            OPTS["c"] = arg
        elif opt in ("-t", "--topics"):
            OPTS["t"] = bool(int(arg))
        elif opt in ("-g", "--graph"):
            OPTS["g"] = bool(int(arg))
        elif opt in ("--num_topics"):
            OPTS["num_topics"] = int(arg)
        elif opt in ("--load_topics"):
            OPTS["load_topics"] = bool(int(arg))
        elif opt in ("--topics_column"):
            if arg not in TOPIC_COLUMN_OPTS:
                usage()
            OPTS["topics_column"] = arg

    run()


if __name__ == "__main__":
    prepare(sys.argv[1:])
