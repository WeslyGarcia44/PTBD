# Generated by Django 4.1.13 on 2023-11-12 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneroVideojuego',
            fields=[
                ('nombre', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('fecha_lanzamiento', models.DateField()),
                ('descripcion', models.TextField()),
                ('genero_videojuego', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.generovideojuego')),
            ],
        ),
    ]
