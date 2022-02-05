# Generated by Django 4.0 on 2022-02-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bachelor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'Бакалавриат',
                'verbose_name_plural': 'Бакалавриат',
            },
        ),
        migrations.CreateModel(
            name='Forms_training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': 'Формы обучения',
                'verbose_name_plural': 'Формы обучения',
            },
        ),
    ]