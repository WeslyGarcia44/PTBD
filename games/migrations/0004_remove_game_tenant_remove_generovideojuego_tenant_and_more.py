# Generated by Django 4.1.13 on 2023-11-19 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_tenant_generovideojuego_tenant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='generovideojuego',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='usergamelist',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='videojuego',
            name='tenant',
        ),
    ]