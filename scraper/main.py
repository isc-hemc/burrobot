"""main.

Prepares and execute the functions in charge to download and store the messages
retrieved from Facebook Messenger thanks to Facebook's Graph API.

To run this script it's necessary to have an access token for Graph API and
in case that the retrieved information will be stored in a Mongo Database
the credentials for the DB must be in the .env file, for more information
check the README.md in this folder or type in the command line:

    > pipenv run python main.py --help

"""
import getopt
import os
import sys
from typing import List, Union

from miner.miner import Miner
from store.file_system import FileSystem
from store.mongo import Mongo
from utils.compere import compere
from utils.config import ACCESS_TOKEN
from utils.custom_classes import Me
from utils.usage import usage


PATH = os.path.dirname(os.path.abspath(__file__))


OPTS = {
    "q": 0,
    "t": 5 * 60,
    "all_data": True,
    "output_path": f"{PATH}/data/",
    "db": False,
}


def run():
    """Run.

    Given the command line arguments, will start the process of information
    retrieval.

    """
    # TODO(davestring/JoseRicardoL): Improve this function.
    # TODO(davestring/JoseRicardoL): OPTS['all_data'] isn't been used.
    # TODO(davestring/JoseRicardoL): OPTS['q'] isn't been used.
    # TODO(davestring/JoseRicardoL): OPTS['t'] isn't been used.
    miner: Miner = Miner(access_token=ACCESS_TOKEN)
    store: Union[FileSystem, Mongo] = FileSystem(OPTS["output_path"])
    if OPTS["db"]:
        store = Mongo("conversations")
    me: Me = miner.me()
    for con in miner.get_all(id_=me.id, conn_name="conversations"):
        fields: str = "messages{message,from,created_time,to}"
        dataset = miner.get(id_=con.id, fields=fields)["messages"]["data"]
        for data in dataset:
            if OPTS["db"]:
                store.upsert(doc=data)
                continue
            store.write(
                data=data,
                file_name=data["created_time"],
                nested_dirs=con.id,
            )


def prepare(argv: List):
    """Prepare.

    Takes the arguments from the command line to prepare the information
    retrieval.

    Parameters
    ----------
    argv: List
        Command line arguments.

    Raises
    ------
    ValueError
        If -q, --quantity parameter is lower than 1.
    ValueError
        If -t, --timeout is lower than 1.

    """
    compere()
    try:
        args: List = ["quantity=", "timeout=", "database=", "help"]
        opts, args = getopt.getopt(argv, "q:t:d:h", args)
    except getopt.GetoptError:
        usage(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-q", "--quantity"):
            quantity: int = int(arg)
            if quantity < 1:
                raise ValueError("Quantity should be greater than 0")
            OPTS["q"] = quantity
            OPTS["all_data"] = False
        elif opt in ("-t", "--timeout"):
            timeout: int = int(arg)
            if timeout < 1:
                raise ValueError("Timeout should be greater than 0")
            OPTS["t"] = timeout * 60
        elif opt in ("-d", "--database"):
            db: bool = bool(int(arg))
            OPTS["db"] = db

    if OPTS["all_data"]:
        print("\nRetrieving all conversations.\n")
    if OPTS["db"]:
        print(f"Retrieved data will be stored in mongo.\n")
    else:
        print(f"Retrieved data will be stored in {OPTS['output_path']}.\n")

    run()


if __name__ == "__main__":
    prepare(sys.argv[1:])
