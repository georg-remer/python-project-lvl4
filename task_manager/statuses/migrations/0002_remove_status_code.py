# Generated by Django 3.2.7 on 2021-09-28 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='code',
        ),
    ]