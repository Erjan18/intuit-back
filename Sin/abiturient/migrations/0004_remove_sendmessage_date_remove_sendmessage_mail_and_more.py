# Generated by Django 4.0 on 2022-01-04 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abiturient', '0003_sendmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sendmessage',
            name='date',
        ),
        migrations.RemoveField(
            model_name='sendmessage',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='sendmessage',
            name='number',
        ),
    ]
