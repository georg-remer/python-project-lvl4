from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Label


class LabelTest(TestCase):

    fixtures = ['users.json', 'labels.json']

    def setUp(self):
        user = get_user_model().objects.first()
        password = 'nO5xDnT8oY9H'
        self.client.login(
            username=user.username,
            password=password,
        )

    def assertLabel(self, label, data):
        self.assertEqual(label.name, data['name'])

    def test_get_labels(self):
        """Tests GET /labels/"""
        response = self.client.get(reverse('labels:list'))
        self.assertEqual(response.status_code, 200)

    def test_get_labels_create(self):
        """Tests GET /labels/create/"""
        response = self.client.get(reverse('labels:create'))
        self.assertEqual(response.status_code, 200)

    def test_post_labels_create(self):
        """Tests POST /labels/create/"""
        label_to_create = {
            'name': 'Test',
        }
        response = self.client.post(reverse('labels:create'), label_to_create)

        self.assertRedirects(response, reverse('labels:list'))
        label = Label.objects.get(name=label_to_create['name'])
        self.assertLabel(label, label_to_create)

    def test_get_labels_update(self):
        """Tests GET /labels/<int:pk>/update/"""
        label = Label.objects.first()
        response = self.client.get(reverse('labels:update', args=[label.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_labels_update(self):
        """Tests POST /labels/<int:pk>/update/"""
        label = Label.objects.first()
        old_name = label.name
        new_name = old_name[::-1]
        label_to_update = {
            'name': new_name,
        }
        response = self.client.post(
            reverse('labels:update', args=[label.pk]),
            label_to_update,
        )
        self.assertRedirects(response, reverse('labels:list'))
        label.refresh_from_db()
        self.assertEqual(label.name, new_name)

    def test_get_labels_delete(self):
        """Tests GET /labels/<int:pk>/delete/"""
        label = Label.objects.first()
        response = self.client.get(reverse('labels:delete', args=[label.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_labels_delete(self):
        """Tests POST /labels/<int:pk>/delete/"""
        label = Label.objects.first()
        response = self.client.post(reverse('labels:delete', args=[label.pk]))
        self.assertRedirects(response, reverse('labels:list'))
        self.assertEqual(Label.objects.count(), 0)
