# Generated by Django 4.1.5 on 2023-01-13 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfilUser', '0008_alter_usuario_options'),
        ('Postagem', '0009_alter_categoria_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentário',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Postagem.post')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfilUser.usuario')),
            ],
        ),
    ]
