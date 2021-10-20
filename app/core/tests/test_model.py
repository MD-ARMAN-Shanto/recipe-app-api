from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserModel(TestCase):

    def test_user_model(self):
        """Test create a new user model"""
        email = 'arman@gmail.com'
        password = 'arman123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))