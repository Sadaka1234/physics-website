# Generated by Django 2.2.1 on 2019-10-17 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudio_usuario',
            name='fecha',
        ),
    ]
