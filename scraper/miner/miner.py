"""miner.

The purpose of this module it's only to mine Facebook Messenger conversations
from a user profile or a creator page. GET request are only supported by the
moment, if the requirements change in the future the new features will be
added.

"""
from typing import Dict, Generator

from facebook import GraphAPI

from utils.custom_classes import Conversation, Me, Message


class Miner:
    """Miner.

    Helper class to get information from a user profile or a facebook page.

    Attributes
    ----------
    access_token: str
        Facebook Graph API application token.
    api: GraphAPI
        A client for the Facebook Graph API.

    """

    __slots__ = ("access_token", "api")

    def __init__(self, access_token: str):
        """Constructor.

        Parameters
        ----------
        access_token: str
            Facebook Graph API application token.

        """
        self.access_token = access_token
        self.api = self.__connection

    @property
    def __connection(self) -> GraphAPI:
        """Connection.

        Established the connection to Graph API with the given token attribute.

        Returns
        -------
        GraphAPI
            A client for the Facebook Graph API.

        """
        return GraphAPI(access_token=self.access_token, version="3.0")

    def me(self) -> Me:
        """Me.

        Retrieves the current client information.

        Returns
        -------
        Me

        """
        return Me(**self.api.get_object(id="me"))

    def get(self, id_: str, fields: str) -> Dict:
        """GET Request.

        Makes a GET request to fetch an object from the graph, this method
        doesn't return all the data from the graph, instead the response comes
        with a cursor to retrieve the next set of data if there is more than
        one element.

        Parameters
        ----------
        id_: str
            ID in a format similar to t_000000000000000.
        fields: str
            Elements that the response must comes with.

        Returns
        -------
        Dict

        """
        return self.api.get_object(id=id_, fields=fields)

    def get_all(self, id_: str, connection_name: str) -> Generator:
        """GET all Request.

        Iterates over all pages returned by a GraphAPI.get_connections call and
        yields the individual items. This request is describes in the form:
        "https://graph.facebook.com/v4.0/{id}/{connection_name}?access_token=access_token"

        Parameters
        ----------
        id_: str
            ID in a format similar to t_000000000000000 or 'me'.
        connection_name: str
            Specifies the connection or edge between objects. By the moment
            the only supported connections are 'conversations' and 'messages'.

        Returns
        -------
        Generator

        """
        # TODO(davestring): By the moment, only supports connection_name type
        # 'conversations' and 'messages', search for a way to make this method
        # generic.
        for el in self.api.get_all_connections(id_, connection_name):
            if connection_name == "conversations":
                yield Conversation(**el)
            if connection_name == "messages":
                yield Message(**el)
