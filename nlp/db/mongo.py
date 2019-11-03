"""mongo.

Connects to a MongoDB using a client-side representation of a MongoDB cluster.

"""
import time
from typing import Dict, Generator, Optional

from bson import ObjectId
from bson.codec_options import CodecOptions
from pymongo import MongoClient
from pymongo.collection import Collection, InsertOneResult

from utils.config import (
    MONGO_DB,
    MONGO_DB_PASSWORD,
    MONGO_DB_USER,
    MONGO_HOST,
    MONGO_PORT,
)


class Mongo:
    """Mongo.

    Using PyMongo establish a connection to a MongoDB server and performs
    actions over the target database.

    Attributes
    ----------
    client: MongoClient
        A client-side representation of a MongoDB cluster.
    collection: Collection
        MongoDB target collection name.

    """

    __slots__ = ("client", "__collection", "__write_concern")

    def __init__(self, collection: str):
        """Constructor.

        Parameters
        ----------
        collection: Collection
            MongoDB target collection name.

        """
        self.client = self.__client
        self.__collection = self.__get_collection(collection)
        self.__write_concern = {
            "writeConcern": {"w": "majority", "wtimeout": 1000}
        }

    @property
    def __client(self) -> MongoClient:
        """Client.

        Creates a client-side representation of a MongoDB cluster.

        Returns
        -------
        MongoClient

        """
        return MongoClient(
            host=MONGO_HOST,
            port=MONGO_PORT,
            username=MONGO_DB_USER,
            password=MONGO_DB_PASSWORD,
            authSource=MONGO_DB,
        )

    def __get_collection(self, collection: str) -> Collection:
        """Get Collection.

        Get a MongoDB collection to perform CRUD actions.

        Parameters
        ----------
        collection: Collection
            MongoDB target collection name.

        Returns
        -------
        Collection

        """
        options: CodecOptions = CodecOptions(tz_aware=True)
        return self.client[MONGO_DB].get_collection(
            collection, codec_options=options
        )

    def find(self) -> Generator:
        """Find.

        Builds a generator with all the documents in the given collection.

        Returns
        -------
        Generator

        """
        return self.__collection.find()

    def find_one(self, query: Dict) -> Optional[Dict]:
        """Find One.

        Search for a document in the give collection.

        Parameters
        ----------
        query: Dict
            Query to perform the search.

        Returns
        -------
        Dict, None

        """
        if "_id" in query:
            query["_id"] = ObjectId(query.pop("_id"))
        return self.__collection.find_one(query)

    def upsert(self, doc: Dict, attempts: int = 0) -> Dict:
        """Upsert.

        Insert or update a document in the given collection.

        Parameters
        ----------
        doc: Dict
            Document to insert in the collection.
        attempts: int
            Attempts trying to store the document.

        Raises
        ------
        ConnectionError
            If the document cannot be stored in the collection.

        Returns
        -------
        Dict
            Inserted document.

        """
        if attempts > 3:
            raise ConnectionError("Cannot connect to MongoDB.")
        if attempts > 0:
            time.sleep(0.001)
        if "_id" in doc:
            _id = doc.pop("_id")
            if isinstance(_id, str):
                _id = ObjectId(_id)
            return self.__collection.find_one_and_replace({"_id": _id}, doc)
        try:
            item: InsertOneResult = self.__collection.insert_one(
                doc, self.__write_concern
            )
        except Exception:
            self.upsert(doc, attempts + 1)
        if (
            isinstance(item, InsertOneResult)
            and getattr(item, "inserted_id") is None
        ):
            return self.upsert(doc, attempts + 1)
        doc["_id"] = item.inserted_id
        return doc
