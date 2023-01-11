# Generated by Django 4.1.5 on 2023-01-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfilUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='escolha',
        ),
        migrations.AddField(
            model_name='usuario',
            name='sexo_usuario',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminio')], default=('M', 'Masculino'), max_length=1),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('AD', 'Administrador'), ('AU', 'Autor'), ('CO', 'Comum')], default=('AD', 'Administrador'), max_length=2),
        ),
    ]