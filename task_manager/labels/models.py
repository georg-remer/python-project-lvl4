from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    created_at = models.DateTimeField(_('created date'), default=timezone.now)
    name = models.CharField(_('name'), max_length=250, unique=True)

    def get_absolute_url(self):
        return reverse('labels:list')

    def __str__(self):
        return self.name
