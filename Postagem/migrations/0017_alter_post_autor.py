# Generated by Django 4.1.5 on 2023-01-17 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfilUser', '0008_alter_usuario_options'),
        ('Postagem', '0016_alter_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='perfilUser.usuario'),
        ),
    ]