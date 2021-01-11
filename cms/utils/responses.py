"""HTTP responses module."""

from rest_framework import status
from rest_framework.response import Response


class CustomResponse:
    """CustomResponse.

    Create a Custom HTTP response that covers the success and error cases.

    Attributes
    ----------
    message : str, default=None
        HTTP response message.
    data : dict, default=None
        HTTP response data.
    headers : dict, default=None
        HTTP response headers.

    Methods
    -------
    success(status_code=status.HTTP_200_OK)
        Creates a success HTTP response with a status code from 200 to 226.
    error(status_code=status.HTTP_400_BAD_REQUEST)
        Creates an error HTTP response with a status code from 400 to 521.

    """

    __slots__ = ("message", "data", "headers")

    def __init__(self, message=None, data=None, headers=None):
        """Class constructor.

        Initializes the `message`, 'data`and `headers` attributes.

        """
        self.message = message
        self.data = data
        self.headers = headers

    def success(self, status_code=status.HTTP_200_OK):
        """Success.

        Returns a success HTTP response.

        Parameters
        ----------
        status_code : int
            HTTP status code, goes from 200 to 226.

        """
        if status_code < 200 or status_code > 226:
            raise ValueError("Invalid HTTP status code.")
        return Response(
            {"message": self.message, "data": self.data},
            status_code,
            headers=self.headers,
        )

    def error(self, status_code=status.HTTP_400_BAD_REQUEST):
        """Error.

        Returns an error HTTP response.

        Parameters
        ----------
        status_code : int
            HTTP status code, goes from 400 to 521.

        """
        if status_code < 400 or status_code > 521:
            raise ValueError("Invalid HTTP status code.")
        return Response(
            {"message": self.message, "errors": self.data},
            status_code,
            headers=self.headers,
        )
