"""Context apps module."""

from django.apps import AppConfig


class ContextConfig(AppConfig):
    """ContextConfig.

    Extends from AppConfig for configure the Context application.

    Attributes
    ----------
    name : str
        Application name.

    """

    name = 'context'
