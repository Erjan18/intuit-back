# Generated by Django 4.0 on 2022-02-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magistracy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magistracy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'Магистратура',
                'verbose_name_plural': 'Магистратура',
            },
        ),
        migrations.RenameModel(
            old_name='Aspirantura',
            new_name='Enactus',
        ),
        migrations.RenameModel(
            old_name='Jobspirant',
            new_name='Jobmagis',
        ),
        migrations.AlterModelOptions(
            name='enactus',
            options={'verbose_name': 'Энактус', 'verbose_name_plural': 'Энактус'},
        ),
        migrations.AlterModelOptions(
            name='jobmagis',
            options={'verbose_name': 'Трудоустройство магистрантов', 'verbose_name_plural': 'Трудоустройство магистрантов'},
        ),
    ]
