# Generated by Django 4.1.13 on 2023-11-21 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0003_game_tenant_generovideojuego_tenant_and_more'),
        ('users', '0003_friendship'),
        ('Game_Developer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('fecha', models.DateField()),
                ('desarrolladora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Game_Developer.desarrolladoravideojuego')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usuario')),
                ('videojuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.videojuego')),
            ],
        ),
    ]
