# Generated by Django 4.1.5 on 2023-01-12 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Postagem', '0007_remove_post_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
    ]