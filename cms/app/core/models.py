"""Core models module."""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    """CustomUserManager.

    Implements utilities for the CustomUser Model.

    Methods
    -------
    create_user(email='', password='', **kwargs)
        Create a new user and persists it into the database.

    """

    def create_user(self, email: str, password: str, **kwargs: dict):
        """Create User.

        Create a new user and persists it into the database.

        Parameters
        ----------
        email : str
            User email address.
        password : str
            User custom password.
        kwargs : dict
            User custom parameters.

        """
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str):
        """Create Superuser.

        Create a new superuser and persists it into the database.

        Parameters
        ----------
        email : str
            Superuser email address.
        password : str
            Superuser custom password.

        """
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """CustomUser Model.

    Extends the AbstractBaseUser class and defines the custom fields for a
    new application User.

    Attributes
    ----------
    email : EmailField
        User email address.
    name : CharField
        User name.
    lastname : CharField
        User lastname.
    is_active : BooleanField
        True if the user is active, otherwise False.
    is_staff : BooleanField
        True if the user is allowed to have access to the admin site.
    objects : CustomUserManager
        Utility methods.
    USERNAME_FIELD : str
        Name descriptor of the field on the user model that will be used as
        unique identifier.

    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
