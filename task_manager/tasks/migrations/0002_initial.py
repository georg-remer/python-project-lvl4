# Generated by Django 3.2.7 on 2021-09-29 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('statuses', '0001_initial'),
        ('labels', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creator',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='creator',
                to=settings.AUTH_USER_MODEL,
                verbose_name='creator',
            ),
        ),
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='executor',
                to=settings.AUTH_USER_MODEL,
                verbose_name='executor',
            ),
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(
                blank=True,
                related_name='labels',
                through='tasks.TaskLabels',
                to='labels.Label',
                verbose_name='labels',
            ),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='status',
                to='statuses.status',
                verbose_name='status',
            ),
        ),
    ]
