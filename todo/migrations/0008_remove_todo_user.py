# Generated by Django 3.1.4 on 2021-01-04 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]