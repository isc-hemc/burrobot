"""tasks."""
from typing import Dict

from db.mongo import Mongo
from db.mysql import SQL
from nlpmodels.text_processing import PreProcessor


def preprocess(opts: Dict, path: str):
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
            ns_nl = pp.rmstopwords(tokens)
            ns_wl = pp.lemmatize(ns_nl)
            ws_wl = pp.lemmatize(tokens)
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
