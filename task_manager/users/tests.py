from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UserTest(TestCase):

    fixtures = ['users.json']

    def assertUser(self, user, data):
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])
        self.assertEqual(user.username, data['username'])

    def test_get_users(self):
        """Tests GET /users/"""
        response = self.client.get(reverse('users:list'))
        self.assertEqual(response.status_code, 200)

    def test_get_users_create(self):
        """Tests GET /users/create/"""
        response = self.client.get(reverse('users:create'))
        self.assertEqual(response.status_code, 200)

    def test_post_users_create(self):
        """Tests POST /users/create/"""
        user_to_create = {
            'first_name': 'John',
            'last_name': 'Smith',
            'username': 'jsmith',
            'password1': 'asgkjKJKJ98',
            'password2': 'asgkjKJKJ98',
        }
        response = self.client.post(reverse('users:create'), user_to_create)

        self.assertRedirects(response, reverse('login'))
        user = get_user_model().objects.get(username=user_to_create['username'])
        self.assertUser(user, user_to_create)

    def test_get_users_update(self):
        """Tests GET /users/<int:pk>/update/"""
        user = get_user_model().objects.first()
        password = 'nO5xDnT8oY9H'
        response = self.client.login(
            username=user.username,
            password=password,
        )
        self.assertTrue(response)
        response = self.client.get(reverse('users:update', args=[user.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_users_update(self):
        """Tests POST /users/<int:pk>/update/"""
        user = get_user_model().objects.first()
        password = 'nO5xDnT8oY9H'
        old_username = user.username
        new_username = old_username[::-1]

        response = self.client.login(
            username=user.username,
            password=password,
        )
        self.assertTrue(response)

        user_to_update = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': new_username,
            'password1': password,
            'password2': password,
        }
        response = self.client.post(
            reverse('users:update', args=[user.pk]),
            user_to_update,
        )
        self.assertRedirects(response, reverse('users:list'))
        user.refresh_from_db()
        self.assertEqual(user.username, new_username)

    def test_get_users_delete(self):
        """Tests GET /users/<int:pk>/delete/"""
        user = get_user_model().objects.first()
        password = 'nO5xDnT8oY9H'
        response = self.client.login(
            username=user.username,
            password=password,
        )
        self.assertTrue(response)
        response = self.client.get(reverse('users:delete', args=[user.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_users_delete(self):
        """Tests POST /users/<int:pk>/delete/"""
        user = get_user_model().objects.first()
        password = 'nO5xDnT8oY9H'
        response = self.client.login(
            username=user.username,
            password=password,
        )
        self.assertTrue(response)
        response = self.client.post(reverse('users:delete', args=[user.pk]))
        self.assertRedirects(response, reverse('users:list'))
        self.assertEqual(get_user_model().objects.count(), 0)

    def test_get_login(self):
        """Tests GET /login/"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_post_login(self):
        """Tests POST /login/"""
        user = get_user_model().objects.first()
        password = 'nO5xDnT8oY9H'
        credentials = {
            'username': user.username,
            'password': password,
        }
        response = self.client.post(reverse('login'), credentials)
        self.assertRedirects(response, reverse('index'))

    def test_post_logout(self):
        """Tests POST /logout/"""
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('index'))
