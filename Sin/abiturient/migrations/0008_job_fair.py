# Generated by Django 4.0 on 2022-01-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturient', '0007_career_delete_sendmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_fair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]
