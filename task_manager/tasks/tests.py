from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskTest(TestCase):

    fixtures = ['users.json', 'statuses.json', 'tasks.json']

    def setUp(self):
        user = get_user_model().objects.first()
        password = 'nO5xDnT8oY9H'
        self.client.login(
            username=user.username,
            password=password,
        )

    def assertTask(self, task, data):
        self.assertEqual(task.name, data['name'])
        self.assertEqual(task.description, data['description'])
        self.assertEqual(task.status.id, data['status'])
        self.assertEqual(task.responsible.id, data['responsible'])

    def test_get_tasks(self):
        """Tests GET /tasks/"""
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, 200)

    def test_get_tasks_create(self):
        """Tests GET /tasks/create/"""
        response = self.client.get(reverse('tasks:create'))
        self.assertEqual(response.status_code, 200)

    def test_post_tasks_create(self):
        """Tests POST /tasks/create/"""
        task_to_create = {
            'name': 'Test',
            'description': 'Test description',
            'status': 1,
            'responsible': 9,
        }
        response = self.client.post(reverse('tasks:create'), task_to_create)

        self.assertRedirects(response, reverse('tasks:list'))
        task = Task.objects.get(name=task_to_create['name'])
        self.assertTask(task, task_to_create)

    def test_get_tasks_update(self):
        """Tests GET /tasks/<int:pk>/update/"""
        task = Task.objects.first()
        response = self.client.get(reverse('tasks:update', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_tasks_update(self):
        """Tests POST /tasks/<int:pk>/update/"""
        task = Task.objects.first()
        old_name = task.name
        new_name = old_name[::-1]
        task_to_update = {
            'name': new_name,
            'description': 'Test description',
            'status': 1,
            'responsible': 9,
        }
        response = self.client.post(
            reverse('tasks:update', args=[task.pk]),
            task_to_update,
        )
        self.assertRedirects(response, reverse('tasks:list'))
        task.refresh_from_db()
        self.assertEqual(task.name, new_name)

    def test_get_tasks_delete(self):
        """Tests GET /tasks/<int:pk>/delete/"""
        task = Task.objects.first()
        response = self.client.get(reverse('tasks:delete', args=[task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_tasks_delete(self):
        """Tests POST /tasks/<int:pk>/delete/"""
        task = Task.objects.first()
        response = self.client.post(reverse('tasks:delete', args=[task.pk]))
        self.assertRedirects(response, reverse('tasks:list'))
        self.assertEqual(Task.objects.count(), 0)

    def test_get_tasks_detail(self):
        """Tests GET /tasks/<int:pk>/"""
        task = Task.objects.first()
        response = self.client.get(reverse('tasks:detail', args=[task.pk]))
        self.assertEqual(response.status_code, 200)
