# Generated by Django 4.2.7 on 2023-12-03 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('cantidad_alumnxs', models.IntegerField()),
                ('turno', models.CharField(max_length=15)),
                ('docente', models.CharField(max_length=40)),
            ],
        ),
    ]
