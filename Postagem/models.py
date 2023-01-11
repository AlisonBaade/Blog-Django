from django.db import models
from perfilUser.models import Usuario
from datetime import datetime


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    

class Post(models.Model):
    imagem = models.ImageField(upload_to='img_principal', null=True, blank=True)
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    autor = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    data_cadastro = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.titulo

