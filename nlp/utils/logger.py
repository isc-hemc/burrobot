"""logger.

NLP log configuration using the standard library.

"""
import logging
import logging.config
import yaml
from logging import Logger


def get_logger(path: str) -> Logger:
    """Get Logger.

    Builds the logging configuration to be used in the application.

    Parameters
    ----------
    path: str
        Location of the root of the project.

    Returns
    -------
    Logger
        Class to handle logs.

    """
    path = f"{path}/logs/config.yaml"
    with open(path, "r") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    return logging.getLogger("nlpLogger")
