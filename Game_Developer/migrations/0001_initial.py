# Generated by Django 4.1.13 on 2023-11-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesarrolladoraVideojuego',
            fields=[
                ('nombre', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('pais', models.CharField(max_length=100)),
                ('fechaFundacion', models.DateField()),
            ],
        ),
    ]
