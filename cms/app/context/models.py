"""Context models module."""

from django.db import models


class Context(models.Model):
    """Context Model.

    Create the Context model and map it to a single database table.

    Attributes
    ----------
    name : CharField
        Context name.
    description : TextField
        Context itself.
    is_active : BooleanField
        True if the context is active, otherwise False.

    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
