# Generated by Django 3.2.7 on 2021-09-26 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0002_alter_task_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLabels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='labels.label')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', through='tasks.TaskLabels', to='labels.Label', verbose_name='labels'),
        ),
    ]