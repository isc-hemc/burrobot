"""Core admin module."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from ..core import models


class CustomUserAdmin(BaseUserAdmin):
    """CustomUserAdmin.

    Defines the actions that will be show in the Django Admin for the
    CustomUser model.

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
    add_fieldsets : Tuple
        Use this attribute when creating a custom user.

    """

    ordering = ["id"]
    search_fields = ("id", "email")
    list_display = [
        "id",
        "email",
        "name",
        "lastname",
        "is_active",
        "is_superuser",
    ]

    fieldsets = (
        (None, {"fields": ("email",)}),
        (_("Personal Info"), {"fields": ("name", "lastname")}),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser")},
        ),
    )

    def has_add_permission(self, request) -> bool:
        """has_add_permission.

        Enables the Create functionality in the Django Admin.

        Returns
        -------
        True if adding an object is permitted, False otherwise.

        """
        return False


admin.site.register(models.CustomUser, CustomUserAdmin)
