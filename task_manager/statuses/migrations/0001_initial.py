# Generated by Django 3.2.7 on 2021-09-27 15:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date')),
                ('code', models.IntegerField(unique=True, verbose_name='code')),
                ('name', models.TextField(unique=True, verbose_name='name')),
            ],
        ),
    ]
