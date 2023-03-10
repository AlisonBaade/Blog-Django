# Generated by Django 4.1.5 on 2023-01-11 18:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfilUser', '0006_rename_tipo_usuario_usuario_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='img_principal')),
                ('titulo', models.CharField(max_length=100)),
                ('data_cadastro', models.DateTimeField(default=datetime.datetime.now)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfilUser.usuario')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Postagem.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
