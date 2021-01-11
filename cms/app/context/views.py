"""Context views module."""

from typing import Optional

from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response
from utils.responses import CustomResponse

from ..context.models import Context
from ..context.serializers import ContextSerializer


class ContextList(views.APIView):
    """ContextList.

    Wrapper that retrieves all the resources from the Context table.

    Methods
    -------
    get(request)
        Retrieves all the resources information of the Context table.

    """

    def get(self, request: Request) -> Response:
        """GET Request.

        Retrieves all the resources information of the Context table.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.

        Returns
        -------
        Response

        """
        queryset = Context.objects.all()
        contexts = ContextSerializer(queryset, many=True).data
        return CustomResponse(
            message="Information as been successfully retrieved", data=contexts
        ).success()


class ContextDetail(views.APIView):
    """ContextDetail.

    Wrapper that allows to perform CRUP operations to a single Context element.

    Methods
    -------
    get_resource(pk)
        Search for a single register in the table Context using the PK.
    get(request, pk)
        Retrieves the detail information of a Context resource.

    """

    def get_resource(self, pk: int) -> Optional[Context]:
        """Get Resource.

        Search for a single register in the table Context using the PK.

        Parameters
        ----------
        pk : int
            Resource primary key.

        Returns
        -------
        Context if the PK exists, otherwise None.

        """
        try:
            return Context.objects.get(pk=pk)
        except Context.DoesNotExist:
            return None

    def get(self, request: Request, pk: int) -> Response:
        """GET Request.

        Retrieves the detail information of a Context resource.

        Parameters
        ----------
        request : Request
            Wrapper allowing to enhance a standard `HttpRequest` instance.
        pk : int
            Resource primary key.

        Returns
        -------
        Response

        """
        queryset = self.get_resource(pk)
        if not queryset:
            return CustomResponse(
                message="The resource doesn't exists."
            ).error(404)

        context = ContextSerializer(queryset).data
        return CustomResponse(message="OK!", data=context).success()
