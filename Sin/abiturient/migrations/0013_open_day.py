# Generated by Django 4.0 on 2022-01-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abiturient', '0012_alter_career_options_alter_description_form_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Open_day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'День открытых дверей',
                'verbose_name_plural': 'День открытых дверей',
            },
        ),
    ]
