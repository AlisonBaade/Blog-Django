# Generated by Django 4.1.5 on 2023-01-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Postagem', '0005_alter_post_conteudo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comentario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]