# Generated by Django 4.1.5 on 2023-01-11 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfilUser', '0005_alter_usuario_data_nascimento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='tipo_usuario',
            new_name='tipo',
        ),
    ]