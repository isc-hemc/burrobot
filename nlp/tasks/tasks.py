"""tasks.

The functions defined in this module perform tasks given the prompt parameters.

"""
from typing import Dict, List

from db.mongo import Mongo
from db.mysql import SQL
from nlp.text_processing import PreProcessor
from nlp.topic_analysis import Topics


def topic_modeling_task(table: str, column: List):
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
    topics = related_topics.print_topics(num_topics=100, num_words=5)
    for topic in topics:
        print(topic)


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
