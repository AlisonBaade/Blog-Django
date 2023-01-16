from django.contrib import admin
from .models import Post, Categoria
from . import models

class ComentarioInLine(admin.TabularInline):
    model = models.Comentario
    extra = 1
    
    
class PostAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioInLine
    ]


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Categoria)
