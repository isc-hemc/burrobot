"""Context admin module."""

from django.contrib import admin
from django.utils.translation import gettext as _

from ..context import models


class ContextAdmin(admin.ModelAdmin):
    """Context Admin.

    Defines the actions that will be show in the Django Admin for the
    Context model.

    Attributes
    ----------
    ordering : List
        Order filter.
    search_fields : Tuple
        Filter options.
    list_display : List
        Columns to be show in the Django Admin.
    fieldsets : Tuple
        Controls the layout of admin “add” and “change” pages.

    """

    ordering = ["id"]
    search_fields = ("id", "name")
    list_display = ["id", "name", "is_active"]

    fieldsets = (
        (None, {"fields": ("name",)}),
        (_("Context Description"), {"fields": ("description",)}),
        (_("Permissions"), {"fields": ("is_active",)}),
    )


admin.site.register(models.Context, ContextAdmin)
