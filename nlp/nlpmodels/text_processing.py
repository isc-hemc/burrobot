"""text processing.

Basically, this module transforms text into a single canonical form.
Normalizing text before storing or processing it allows for separation of
concerns, since input is guaranteed to be consistent before operations are
performed on it.

"""
from typing import Dict, List, Optional
import re

from nltk import word_tokenize

from utils import resources as r


class PreProcessor:
    """PreProcessor.

    This class has the necessary methods for normalazing and preprocessing
    text. The tasks of this module are: lemmatize, tokenize, remove stopwords
    and remove rare characters.

    Attributes
    ----------
    encoders: r.Encodings
        Class that stores the encoding information of the lemmas and stopwords
        files.
    path: str
        Location of the root of the project.
    lemmas: Dict
        Dictionary of lemmas.
    stopwords: List
        List of stopwords.

    """

    __slots__ = ("encoders", "path", "lemmas", "stopwords")

    def __init__(self, path: str):
        """Constructor.

        Parameters
        ----------
        path: str
            Location of the root of the project.

        """
        self.path: str = path
        self.encoders: r.Encodings = r.load_encodings(path=self.path)
        self.lemmas: Dict = self._lemmas
        self.stopwords: List = self._stopwords

    @property
    def _lemmas(self) -> Dict:
        """Lemmas.

        Class property that loads the lemmas dictionary.

        Returns
        -------
        Dict
            Lemmas dictionary.

        """
        return r.load_lemmas(path=self.path, encoder=self.encoders.lemmas)

    @property
    def _stopwords(self) -> List:
        """Stopwords.

        Class property that loads the stopwords list.

        Returns
        -------
        List
            Stopwords list.

        """
        return r.load_stopwords(
            path=self.path, encoder=self.encoders.stopwords
        )

    def rmspecial_characters(
        self, txt: str, regex: str = "[A-ZÁÉÍÓÚÜÑa-záéíóúüñ]+"
    ) -> str:
        """Remove Special Characters.

        Using a regular expression, this method removes every character that's
        not part of the spanish language.

        Parameters
        ----------
        txt: str
            Text to normalize.
        regex: str
            Regular expression for cleaning data.
        
        Returns
        -------
        str
            Text without rare characters.

        """
        return " ".join(re.findall(regex, txt))

    def tokenize(self, txt: str, tolower: bool = True) -> Optional[List]:
        """Tokenize.

        With the help of nltk's word_tokenizer this methos tokenize a text if
        isn't None and isn't an empty string.

        Parameters
        ----------
        txt: str
            Text to normalize.
        tolower: bool
            If it's True transforms the txt string to lower case.

        Returns
        -------
        List, None
            If the text is not None and not an empty string will return the
            text tokenized otherwise None.

        """
        if txt is not None or txt != "":
            txt = txt.lower() if tolower else txt
            return word_tokenize(txt)
        return None

    def rmstopwords(self, tokens: List) -> List:
        """RMStopwords.

        Using the stopwords list defined in the class attributed, removes every
        stopword in the stopwords list.

        Parameters
        ----------
        tokens: List
            Text tokenized.
        
        Returns
        -------
        List
            Text tokenized without stopwords.

        """
        return list(filter(lambda t: t not in self.stopwords, tokens))

    def lemmatize(self, tokens: List) -> List:
        """Lemmatize.

        Using the lemmas dictionary defined in the class attributes, change
        every word in the tokens parameter to its canonical form.

        Parameters
        ----------
        tokens: str
            Text tokenized.

        Returns
        -------
        List
            Text tokenized in its canonical form.

        """
        lemmatized_tokens: List = []
        for t in tokens:
            if t in self.lemmas:
                lemmatized_tokens.append(self.lemmas[t])
        return lemmatized_tokens
