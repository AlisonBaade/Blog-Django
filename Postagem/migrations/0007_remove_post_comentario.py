# Generated by Django 4.1.5 on 2023-01-12 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Postagem', '0006_post_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comentario',
        ),
    ]
