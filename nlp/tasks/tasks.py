"""tasks.

The functions defined in this module perform tasks given the prompt parameters.

"""
import ast
import os
from typing import Dict, List

from db.mongo import Mongo
from db.mysql import SQL
from nlp.text_processing import PreProcessor
from nlp.topic_analysis import Topics
from plotter.plotter import Plotteus
from utils.lda_destructuring import destruct_latend_dirichlet_allocation
from utils.logger import get_logger


def load_topics_task(path: str) -> List:
    """Load Topics.

    Load a list of topics from a `txt` file.

    Parameters
    ----------
    path: str
        Location of the root of the project.

    """
    tpath = f"{path}/resources/topics.txt"
    topics: List = []
    try:
        with open(tpath) as f:
            for topic in f.readlines():
                topic = topic.rstrip()
                topics.append(ast.literal_eval(topic))
        return topics
    except FileNotFoundError as e:
        get_logger(path).error(f"{repr(e)} - {tpath}\n")
        return []


def plot_topics_task(topics: List):
    """Plot Topics.

    Literaly plot the topics passed as argument.

    Parameters
    ----------
    topics: List
        List of topics to plot.

    """
    topics = destruct_latend_dirichlet_allocation(data=topics)
    plotter: Plotteus = Plotteus()
    plotter.style("dark_background")
    for topic in topics:
        setattr(plotter, "data", topic)
        plotter.barplot(
            xlabel="Probability", ylabel="Topic", title="Topic Analysis"
        )


def topic_modeling_task(num_topics: int, table: str, column: List):
    """Topic Modeling.

    Given a corpus, retrieves the more common topics.

    Parameters
    ----------
    table: str
        SQL database table to perform the queries.
    column: List
        Column in the SQL database to retrieve information.

    """
    sql: SQL = SQL()
    sql.set_cursor(cursor_class="Cursor")
    corpus = [row[0] for row in sql.find(table=table, cols=column)]
    topics = Topics(corpus=corpus)
    related_topics = topics.latent_dirichlet_allocation()
    return related_topics.print_topics(num_topics=num_topics, num_words=5)


def preprocess_task(opts: Dict, path: str):
    """PreProcess.

    Downloads the data stored in a NoSQL database and performs a pre-process
    task, i.e., clean the data from rare characters, remove stopwords and
    lemmatize the text, then stores the pre-processed data in a SQL database to
    have easy access to the information.

    Parameters
    ----------
    opts: Dict
        Prompt options passed by the user.
    path: str
        Location of the root of the project.

    """
    # TODO(davestring/JoseRicardoL): Improve this section. A dataclass
    # should work to build the MySQL row.
    # TODO(davestring/JoseRicardoL): Add threads to improve performance.
    pp: PreProcessor = PreProcessor(path=path)
    mongo: Mongo = Mongo(opts["c"])
    sql: SQL = SQL()
    for doc in mongo.find():
        conversation_id = doc["conversation_id"]
        msg_id = doc["id"]
        created_time = doc["created_time"]
        raw_msg = doc["message"].replace("'", "")
        ws_nl = pp.rmspecial_characters(raw_msg)
        if ws_nl:
            tokens = pp.tokenize(ws_nl)
            ws_wl = pp.lemmatize(tokens)
            ns_wl = pp.rmstopwords(ws_wl)
            ns_nl = pp.rmstopwords(tokens)
            conversation = sql.find(
                table="Conversation",
                search_query={"conversation_id": conversation_id},
                first=True,
            )
            if conversation is None:
                sql.upsert(
                    table="Conversation",
                    registry={"conversation_id": conversation_id},
                )
                conversation = sql.find(
                    table="Conversation",
                    search_query={"conversation_id": conversation_id},
                    first=True,
                )
            message = sql.find(
                table="Message", search_query={"msg_id": msg_id}, first=True
            )
            if message is None and ns_wl:
                sql.upsert(
                    table="Message",
                    registry={
                        "msg_id": msg_id,
                        "raw_msg": raw_msg,
                        "no_stopwords_no_lemmas_msg": " ".join(ns_nl),
                        "with_stopwords_no_lemmas_msg": ws_nl,
                        "no_stopwords_with_lemmas_msg": " ".join(ns_wl),
                        "with_stopwords_with_lemmas_msg": " ".join(ws_wl),
                        "created_time": created_time,
                        "conversation_id": conversation["id"],
                    },
                )
