from django.db import models
from datetime import date


class Usuario(models.Model):
    nivel_acesso = (
        ('AD', 'Administrador'),
        ('AU', 'Autor'),
        ('CO', 'Comum')
    )
    sexo = (
        ('M', 'Masculino'),
        ('F', 'Feminio')
    )
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    tipo = models.CharField(max_length=2, choices=nivel_acesso,)
    senha = models.CharField(max_length=64)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo_usuario = models.CharField(max_length=1,choices=sexo, default=sexo[0], blank=True, null=True)
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
