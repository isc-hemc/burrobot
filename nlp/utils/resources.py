"""resources.

In the root folder of this module there is a directory named 'resources' which
stores information like lemmas dictionaries or lists of spanish stopwords, this
module will be in charge of loading those resources to work with them.

"""
import json
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Encodings:
    """Encodings.

    Stores the encodings of the lemmas and stopwords files.

    Attributes
    ----------
    lemmas: str
        Encoding of the lemmas file.
    stopwords: str
        Encoding of the stopwords file.

    """

    lemmas: str
    stopwords: str


def load_encodings(path: str) -> Encodings:
    """Load Encodings.

    Load the encondings of the lemmas and stopwords files.

    Parameters
    ----------
    path: str
        Location of the root of the project.

    Returns
    -------
    Encodings
        A class with the encodings information.

    """
    path = f"{path}/resources/encodings.json"
    with open(path) as f:
        data: Dict = json.load(f)
    return Encodings(**data)


def load_lemmas(path: str, encoder: str) -> Dict:
    """Load Lemmas.

    Load the lemmas file.

    Parameters
    ----------
    path: str
        Location of the root of the project.

    Returns
    -------
    Dict
        Dictionary of lemmas.

    """
    path = f"{path}/resources/lemmas.txt"
    lemmas: Dict = {}
    with open(path, "r", encoding=encoder) as f:
        for line in f.readlines():
            lemma_word: List = line.split()
            if lemma_word != []:
                lemmas[lemma_word[1]] = lemma_word[0]
    return lemmas


def load_stopwords(path: str, encoder: str) -> List:
    """Load Stopwords.

    Load the stopwords file.

    Parameters
    ----------
    path: str
        Location of the root of the project.

    Returns
    -------
    List
        List of stopwords.

    """
    path = f"{path}/resources/stopwords.txt"
    stopwords: List = []
    with open(path, "r", encoding=encoder) as f:
        stopwords = f.read().split("\n")
    return stopwords
