"""custom classes.

Data classes that pretends to make raw data manageable.

"""
from dataclasses import dataclass


@dataclass
class Me:
    """Me.

    Stores the information the current client of the application.

    Attributes
    ----------
    id: str
        ID in a format similar to 000000000000000.
    name: str
        Name of the client.

    """

    id: str
    name: str


@dataclass
class Conversation:
    """Conversation.

    Stores the information of a GraphAPI.get_connection element of type
    conversation.

    Attributes
    ----------
    id: str
        ID in a format similar to t_000000000000000.
    link: str
        Source link.
    updated_time: str
        Last update of the source.

    """

    id: str
    link: str
    updated_time: str


@dataclass
class Message:
    """Message.

    Stores the information of a GraphAPI.get_connection element of type
    message.

    Attributes
    ----------
    id: str
        ID in a format similar to t_000000000000000.
    created_time: str
        Source created date.

    """

    id: str
    created_time: str
