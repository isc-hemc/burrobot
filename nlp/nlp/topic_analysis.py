"""topic analysis.

Using gensim, implements different approaches to retrieve the most common
topics of a corpus.

"""
from typing import List

from nltk import word_tokenize
from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel


class Topics:
    """Topics.

    This class has the necessary methods to retrieve the most common topics
    using different approaches.

    Attributes
    ----------
    corpus: List
        List of documents, where each element is a string.
    tokenized_corpus: List
        List of tokenized documents.

    """

    __slots__ = ("corpus", "tokenized_corpus")

    def __init__(self, corpus: List):
        """Constructor.

        Parameters
        ----------
        corpus: List
            List of documents, where each element is a string.

        """
        self.corpus = corpus
        self.tokenized_corpus = self.__tokenize_corpus

    @property
    def __tokenize_corpus(self) -> List:
        """Tokenize Corpus.

        Class property to tokenize each element of the corpus.

        Returns
        -------
        List
            Tokenized corpus.

        """
        return [word_tokenize(txt) for txt in self.corpus]

    def latent_dirichlet_allocation(
        self, num_topics: int = 100, passes: int = 75
    ) -> LdaModel:
        """Latent Dirichlet Allocation.

        Model estimation from a training corpus and inference of topic
        distribution on new, unseen documents.

        Returns
        -------
        LdaModel
            Latent Dirichlet Allocation trianed model.

        """
        tmp = Dictionary(self.tokenized_corpus)
        aux = [tmp.doc2bow(tokens) for tokens in self.tokenized_corpus]
        return LdaModel(aux, num_topics=num_topics, id2word=tmp, passes=passes)
