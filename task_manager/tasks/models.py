from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status


class Task(models.Model):
    created_at = models.DateTimeField(_('created date'), default=timezone.now)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='created_by',
        verbose_name=_('created_by'),
    )
    name = models.CharField(_('name'), max_length=250, unique=True)
    description = models.TextField(_('description'), blank=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='status',
        verbose_name=_('status'),
    )
    responsible = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='responsible',
        blank=True,
        null=True,
        verbose_name=_('responsible'),
    )

    def get_absolute_url(self):
        return reverse('tasks:list')

    def __str__(self):
        return f'{self.name}'
