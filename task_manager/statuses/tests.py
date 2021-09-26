from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Status


class StatusTest(TestCase):

    fixtures = ['users.json', 'statuses.json']

    def setUp(self):
        user = get_user_model().objects.first()
        password = 'nO5xDnT8oY9H'
        self.client.login(
            username=user.username,
            password=password,
        )

    def assertStatus(self, status, data):
        self.assertEqual(status.code, data['code'])
        self.assertEqual(status.name, data['name'])

    def test_get_statuses(self):
        """Tests GET /statuses/"""
        response = self.client.get(reverse('statuses:list'))
        self.assertEqual(response.status_code, 200)

    def test_get_statuses_create(self):
        """Tests GET /statuses/create/"""
        response = self.client.get(reverse('statuses:create'))
        self.assertEqual(response.status_code, 200)

    def test_post_statuses_create(self):
        """Tests POST /statuses/create/"""
        status_to_create = {
            'code': 0,
            'name': 'Test',
        }
        response = self.client.post(reverse('statuses:create'), status_to_create)

        self.assertRedirects(response, reverse('statuses:list'))
        status = Status.objects.get(code=status_to_create['code'])
        self.assertStatus(status, status_to_create)

    def test_get_statuses_update(self):
        """Tests GET /statuses/<int:pk>/update/"""
        status = Status.objects.first()
        response = self.client.get(reverse('statuses:update', args=[status.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_statuses_update(self):
        """Tests POST /statuses/<int:pk>/update/"""
        status = Status.objects.first()
        old_name = status.name
        new_name = old_name[::-1]
        status_to_update = {
            'code': status.code,
            'name': new_name,
        }
        response = self.client.post(
            reverse('statuses:update', args=[status.pk]),
            status_to_update,
        )
        self.assertRedirects(response, reverse('statuses:list'))
        status.refresh_from_db()
        self.assertEqual(status.name, new_name)

    def test_get_statuses_delete(self):
        """Tests GET /statuses/<int:pk>/delete/"""
        status = Status.objects.first()
        response = self.client.get(reverse('statuses:delete', args=[status.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_statuses_delete(self):
        """Tests POST /statuses/<int:pk>/delete/"""
        status = Status.objects.first()
        response = self.client.post(reverse('statuses:delete', args=[status.pk]))
        self.assertRedirects(response, reverse('statuses:list'))
        self.assertEqual(Status.objects.count(), 0)
