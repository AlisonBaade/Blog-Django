from django.db import models



class Usuario(models.Model):

    autor = models.BooleanField(default=False)
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    

    def __str__(self):
        return self.nome

    
