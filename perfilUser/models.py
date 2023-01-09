from django.db import models



class Usuario(models.Model):
    choices = [('AD', 'Administrador'), ('AU', 'Autor'), ('CO', 'Comum')]

    nome = models.CharField(max_length=50)
    email = models.EmailField()
    tipo = models.CharField(max_length=30, choices=choices)
    senha = models.CharField(max_length=64)
    

    def __str__(self):
        return self.nome
