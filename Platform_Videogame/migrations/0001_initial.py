# Generated by Django 4.1.13 on 2023-11-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlataformaVideojuego',
            fields=[
                ('nombre', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('empresa', models.CharField(max_length=255)),
            ],
        ),
    ]
