# Generated by Django 2.2.1 on 2019-09-12 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topico', models.CharField(max_length=255)),
                ('subtopico', models.CharField(max_length=255)),
            ],
        ),
    ]