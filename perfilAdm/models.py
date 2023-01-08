from django.db import models


class UsuarioAdm(models.Model):
    choice = models.CharField(
        default='A',
        max_length=1,
        choices=(
            ('A', 'Autor'),
            ('M', 'Administrador'),
        )
    )
    nome =  models.CharField(max_length= 50)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    
    def __str__(self):
        return self.nome
    