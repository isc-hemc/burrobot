"""mongo.

Connects to a MySQL database using a client-side representation of a cluster.

"""
import time
from typing import Dict, List, Union

import pymysql

from utils.config import (
    MYSQL_DB,
    MYSQL_DB_PASSWORD,
    MYSQL_DB_USER,
    MYSQL_HOST,
    MYSQL_PORT,
)


class SQL(object):
    """SQL.

    Implements a connection to an SQL Database server.

    Attributes
    ----------
    conn: pymysql.connect
        PyMySQL connection object.
    cursor: pymysql.Connection.cursor
        PyMySQL connection cursos.

    """

    __slots__ = ("conn", "cursor")

    def __init__(self):
        """Constuctor.

        Class constructor.

        """
        self.conn = self.__connect()
        self.cursor = self.conn.cursor()

    @property
    def __headers(self) -> List[str]:
        """Headers.

        Get the headers attached to the cursor.

        Returns
        -------
        List

        """
        return [i[0] for i in self.cursor.description]

    def __connect(self, attempts: int = 0):
        """Connect.

        Connects to a MySQL server.

        Parameters
        ----------
        attempts: int
            Connection attempts.

        Raises
        ------
        ConnectionError
            If the connection can't be established.

        Returns
        -------
        Connect
            PyMySQL connection object.

        """
        if attempts > 3:
            raise ConnectionError("Cannot connect to MySQL.")
        if attempts > 0:
            time.sleep(0.001)
        try:
            return pymysql.connect(
                host=MYSQL_HOST,
                port=MYSQL_PORT,
                user=MYSQL_DB_USER,
                password=MYSQL_DB_PASSWORD,
                db=MYSQL_DB,
                cursorclass=pymysql.cursors.DictCursor,
            )
        except Exception:
            self.__connect(attempts + 1)

    def find(
        self,
        table: str,
        cols: List = [],
        search_query: Dict = {},
        first: bool = False,
        fetch_all: bool = True,
    ) -> Union[Dict, List]:
        """Find.

        Search for a registry in the database.

        Parameters
        ----------
        table: str
            Table in which perform the action.
        cols: List
            Row fields to retrieve, if the value is an empty list then will
            select all fields (*).
        search_query: Dict
            From the rows retrieved performs a WHERE statement to find matches.
        first: bool
            Retrieve the first element in the dataset.
        fetch_all: bool
            Retrieve all the elements of a table.

        Returns
        -------
        List
            Retrieved data.

        """
        query = "SELECT"
        if fetch_all and not cols:
            query += f" * FROM {table}"
        else:
            for col in cols:
                query += f"`{col}`,"
            query = f"{query[:-1]} FROM {table}"
        if search_query:
            query += " WHERE "
            for key, value in search_query.items():
                query += f"`{key}`='{value}' AND "
            query = query[:-5]
        self.cursor.execute(query)
        if first:
            return self.cursor.fetchone()
        return self.cursor.fetchall()

    def upsert(self, table: str, registry: Dict, attempts: int = 0):
        """Upsert.

        Insert or update a registry in the given table.

        Parameters
        ----------
        table: str
            Table in which perform the action.
        registry: Dict
            Registry to update or insert.
        attempts: int
            Action attempts.

        Raises
        ------
        ConnectionError
            If the action can't be performed.

        """
        if attempts > 3:
            raise ConnectionError("Cannot connect to MySQL.")
        if attempts > 0:
            time.sleep(0.001)
        if "id" in registry:
            _id = registry.pop("id")
            query = f"UPDATE `{table}` SET "
            for key, value in registry.items():
                query += f"`{key}`='{value}' "
            query += f"WHERE `id`={_id}"
        else:
            query = f"INSERT INTO `{table}` ("
            keys, values = zip(*registry.items())
            for key in keys:
                query += f"`{key}`,"
            query = f"{query[:-1]}) VALUES ("
            for value in values:
                query += f"'{value}',"
            query = f"{query[:-1]})"
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            self.upsert(table, registry, attempts + 1)

    def reconnect(self):
        """Reconnect.

        If the connection is lost, this method helps to reconnect to the
        database referenced in the constructor.

        """
        self.conn = self.__connect()
        self.cursor = self.conn.cursor()

    def close(self):
        """Close.

        Close the database connection.

        """
        self.conn.close()
