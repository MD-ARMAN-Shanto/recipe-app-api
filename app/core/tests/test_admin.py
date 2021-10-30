from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTestCase(TestCase):
    email = 'arman@gmail.com'
    password = 'arman123'

    def setup(self):
        """setup the test client for admin"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email=self.email,
            password=self.password
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password,
            name='Test User fullname'
        )

    def test_user_listed(self):
        """tested users are listed on the user page"""
        url = reverse('admin:core_users_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
