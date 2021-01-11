"""Context serializers module."""

from rest_framework import serializers

from ..context.models import Context


class ContextSerializer(serializers.ModelSerializer):
    """ContextSerializer.

    Extends from ModelSerializer and convert a queryset of the Context model
    into a native python datatype.

    """

    class Meta:
        """Meta.

        Inner Meta class for the ContextSerializer, it will allow us to add
        custom rules to our serialized information.

        Attributes
        ----------
        model : Context
            Model from where the serializer will retrieve information.
        fields : List
            Fields that will include when serializing the model.
        read_only_fields : Tuple
            Fields that will not be editable when user make POST request.

        """

        model = Context
        fields = ["id", "name", "description", "is_active"]
        read_only_fields = ("id",)
