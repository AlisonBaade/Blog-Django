# Generated by Django 4.1.5 on 2023-01-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfilUser', '0003_usuario_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateField(),
        ),
    ]
