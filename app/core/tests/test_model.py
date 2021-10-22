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

    def test_new_user_model(self):
        """email normalization"""
        email = 'arman@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123456'
        )
        self.assertEqual(user.email, email.lower())

    def test_user_email_not_given(self):
        """The email is not given then raise an exception"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')