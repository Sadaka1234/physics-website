# Generated by Django 2.2.1 on 2019-10-06 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0004_auto_20191006_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudio',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.materia'),
        ),
    ]