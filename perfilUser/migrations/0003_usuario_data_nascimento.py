# Generated by Django 4.1.5 on 2023-01-11 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfilUser', '0002_remove_usuario_escolha_usuario_sexo_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
