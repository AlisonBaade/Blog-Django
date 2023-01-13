from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse
from .models import Categoria, Post
from perfilUser.models import Usuario
from datetime import datetime


def home(request):
        categorias = Categoria.objects.all()
        usuario_req = request.session.get('usuario')
        usuario = Usuario.objects.filter(id=usuario_req)
        if usuario :
            return render(request, 'home.html',{'categorias': categorias,
                                                'usuario_logado': request.session.get('usuario'),
                                                'usuario_autor': usuario,})
        else:
            return HttpResponse('Sem acesso')


def index(request):
    
    categorias = Categoria.objects.filter()
    posts = Post.objects.filter()
    
    return render(request, 'index.html', {'categorias': categorias,
                                          'posts': posts})
    
    
def ver_post(request, id): 
    if request.session.get('usuario'):
        
        post = Post.objects.filter(id = id).first()
        
        return render(request, 'ver_post.html', {'post': post,
                                                 })


def cadastro_post(request):
    
    if request.method == 'POST':
        
        imagem_upload = request.FILES.get('imagem')
        print(imagem_upload)
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
    