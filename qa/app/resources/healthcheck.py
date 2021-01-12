"""healthcheck resource module."""

from flask import Response
from flask_restful import Resource
from utils import CustomResponse


class HealthcheckResource(Resource):
    """HealthcheckResource.

    Resource that expose the Healthcheck endpoints.

    Methods
    -------
    get()
        Retrieve the API status.

    """

    def get(self) -> Response:
        """GET Request.

        Retrieve the API status.

        Returns
        -------
        Response

        """
        return CustomResponse(
            message="API working", data={"status": "ok"}
        ).success()
