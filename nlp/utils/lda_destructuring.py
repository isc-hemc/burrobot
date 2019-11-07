"""lda destructuring.

Given the output of the LDA algorithm used in the `topics_analysis` module,
the methods coded below will destruct the list of topics and will create
a plottable dataset for a better visual comprehension.

"""
import re
from typing import List


def destruct_latend_dirichlet_allocation(data: List) -> List:
    """Destruct Latent Dirichlet Allocation.

    Receives a the output of the LDA algorithm used in `topic_analysis` and
    transforms each element into a dictionary of data.

    Parameters
    ----------
    data: List
        `topic_analysis` LDA output.
    
    Returns
    -------
    List
        List of dictionaries.

    """
    output: List = []
    regex: str = r"(?i)\b[a-záéíóúüñ0-9.*\"]+\b"
    for el in data:
        topics = re.findall(regex, el[1])
        topics = list(map(lambda t: t.split('*"'), topics))
        topics = list(map(lambda t: (t[1], t[0]), topics))
        output.append(dict(topics))
    return output
