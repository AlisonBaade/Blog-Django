# Generated by Django 4.1.5 on 2023-01-13 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfilUser', '0007_alter_usuario_tipo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['nome']},
        ),
    ]
