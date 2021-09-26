from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    def get_absolute_url(self):
        return reverse('users:list')

    def __str__(self):
        return '{full_name}'.format(
            full_name=self.get_full_name(),
        )
