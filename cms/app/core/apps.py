"""Core apps module."""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """CoreConfig.

    Extends from AppConfig for configure the Core application.

    Attributes
    ----------
    name : str
        Application name.

    """

    name = "core"
