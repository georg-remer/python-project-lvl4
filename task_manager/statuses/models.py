from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    created_at = models.DateTimeField(_('created date'), default=timezone.now)
    name = models.TextField(_('name'), unique=True)

    def get_absolute_url(self):
        return reverse('statuses:list')

    def __str__(self):
        return f'{self.name}'
