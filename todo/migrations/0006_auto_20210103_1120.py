# Generated by Django 3.1.4 on 2021-01-03 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todo_published_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoposts',
            options={'ordering': ['-published_date']},
        ),
    ]
