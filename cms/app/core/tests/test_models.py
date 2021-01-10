"""Test cases for Core models."""

from django.contrib.auth import get_user_model
from django.test import TestCase
from faker import Faker


class TestCustomUser(TestCase):
    """Test cases for CustomUser model.

    Methods
    -------
    test_create_user_success()
        Create a user sucess test.

    """

    def setUp(self):
        """Initialize the test attributes."""
        self.faker = Faker("en_US")

    def test_create_custom_user_success(self):
        """Create a new user success test.

        Will create a new user using the `get_user_model` and
        `create_user` function.

        Raises
        ------
        Exception
            If user email or password doesn't match with the created user.

        """
        email = self.faker.email()
        password = self.faker.password()

        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser_success(self):
        """Create a new superuser success test.

        Will create a new superuser using the `get_user_model` and the
        `create_superuser` functions.

        Raises
        ------
        Exception
            If user email or password doesn't match with the created superuser.

        """
        email = self.faker.email()
        password = self.faker.password()

        user = get_user_model().objects.create_superuser(
            email=email, password=password
        )

        self.assertTrue(user.is_superuser)
