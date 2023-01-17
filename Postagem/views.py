from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse
from .models import Categoria, Post, Comentario
from perfilUser.models import Usuario
from datetime import datetime
from django.core.paginator import Paginator


def home(request):
        categorias = Categoria.objects.all()
        usuario_req = request.session.get('usuario')
        usuario = Usuario.objects.filter(id=usuario_req).first()
        usuario_logado = usuario
        if usuario :
            return render(request, 'home.html',{'categorias': categorias,
                                                'usuario_logado': usuario_logado,
                                                'usuario_autor': usuario,})
        else:
            return HttpResponse('Sem acesso')


def index(request):
    if request.session.get('usuario'):  
        categorias = Categoria.objects.filter()
        posts = Post.objects.all()
        posts_paginator = Paginator(posts, 2)
        page_num = request.GET.get('page')
        page = posts_paginator.get_page(page_num)
        usuario = Usuario.objects.filter(id=request.session.get('usuario')).first()
        usuario_logado = usuario

        return render(request, 'index.html', {'categorias': categorias,
                                              'page': page,
                                              'usuario_logado' : usuario_logado})
    
    
def ver_post(request, id): 
    if request.session.get('usuario'):
        posts = Post.objects.filter(id = id)
        usuario = Usuario.objects.filter(id=request.session.get('usuario')).first()
        usuario_logado = usuario
    ############ FILTRAR COMENTÁRIOS DA POSTAGEM ############
        comentarios = Comentario.objects.all()

        return render(request, 'ver_post.html', {'posts': posts,
                                                 'comentarios': comentarios,
                                                 'usuario_logado': usuario_logado})


def cadastro_post(request):
    
    if request.method == 'POST':
        
        imagem_upload = request.FILES.get('imagem', None)

        titulo = request.POST.get('titulo')
        categoria_name = request.POST.get('categoria')
        categoria_filtered = Categoria.objects.filter(nome=categoria_name).first()
        autor = request.POST.get('autor')
        autor_filtered = Usuario.objects.filter(id=autor).first()
        data_cadastro = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        conteudo = request.POST.get('conteudo')
        
        form = Post(
            imagem=imagem_upload,
            titulo=titulo,
            categoria=categoria_filtered,
            autor=autor_filtered,
            data_cadastro=data_cadastro,
            conteudo=conteudo
        )
        if form:
            form.save()
            return redirect('/posts/home/?status=0')
        else:
            return redirect('/posts/home/?status=1')
    