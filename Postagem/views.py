from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse
from .models import Categoria, Post, Comentario
from perfilUser.models import Usuario
from datetime import datetime
from django.core.paginator import Paginator


def home(request):
        usuario_req = request.session.get('usuario')
        usuario = Usuario.objects.filter(id=usuario_req).first()
        usuario_logado = usuario
        post = Post.objects.filter(autor=usuario)
        qnt_post = post.count()
        if usuario :
            return render(request, 'home.html',{'usuario_logado' : usuario_logado,
                                                'usuario_autor' : usuario,
                                                'post': post,
                                                'qnt_post' : qnt_post})
        else:
            return HttpResponse('Sem acesso')


def index(request):
    if request.session.get('usuario'):  
        categorias = Categoria.objects.filter()
        posts = Post.objects.all()
        posts_paginator = Paginator(posts, 10)
        page_num = request.GET.get('page')
        page = posts_paginator.get_page(page_num)
        usuario = Usuario.objects.filter(id=request.session.get('usuario')).first()
        usuario_logado = usuario

        return render(request, 'index.html', {'categorias': categorias,
                                              'page': page,
                                              'usuario_logado' : usuario_logado})
    
    
def ver_post(request, id): 
    if request.session.get('usuario'):
        post = Post.objects.filter(id = id).first()
        usuario = Usuario.objects.filter(id=request.session.get('usuario')).first()
        usuario_logado = usuario
        comentarios = Comentario.objects.filter(post=id)

        return render(request, 'ver_post.html', {'post': post,
                                                 'comentarios': comentarios,
                                                 'usuario_logado': usuario_logado})


def edit_post(request, id):
    if request.session.get('usuario'):
        post = Post.objects.filter(id = id).first()
        categorias = Categoria.objects.all()
        usuario_req = request.session.get('usuario')
        usuario = Usuario.objects.filter(id=usuario_req).first()
        usuario_logado = usuario
        return render(request, 'edit_post.html', {'post' : post,
                                                  'categorias' : categorias,
                                                  'usuario_logado' : usuario_logado})

def cadastrar_post(request):
    # PÁGINA DE CADASTRO DE POSTAGEM
    if request.session.get('usuario'):
        usuario_req = request.session.get('usuario')
        usuario = Usuario.objects.filter(id=usuario_req).first()
        usuario_logado = usuario
        categorias = Categoria.objects.all()
        status = request.GET.get('status')
        return render(request, 'cadastrar_post.html', {'categorias' : categorias,
                                                       'usuario_logado' : usuario_logado,
                                                       'usuario_req' : usuario_req,
                                                       'status' : status})



def cadastro_post(request):
    # FORMULÁRIO DE CADASTRO DA POSTAGEM
    if request.method == 'POST':
        
        imagem_upload = request.FILES.get('imagem', None)
        if imagem_upload == None:
            imagem_upload = 'img_principal/sem-img.jpg'
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
            return redirect('/posts/cadastrar_post/?status=0')
        else:
            return redirect('/posts/cadastrar_post/?status=1')
    
    
def excluir_post(request, id):
    if request.session.get('usuario'):
        post = Post.objects.filter(id=id).delete()
        return redirect('/posts/home')
    
    
def alterar_post(request, id):

    imagem_upload = request.FILES.get('imagem', None)
    if imagem_upload == None:
        imagem_upload = 'img_principal/sem-img.jpg'
    titulo = request.POST.get('titulo')
    categoria = request.POST.get('categoria')
    categoria_filtered = Categoria.objects.filter(nome=categoria).first()
    conteudo = request.POST.get('conteudo')
    
    post = Post.objects.get(id=id)
    
    if post.autor.id == request.session['usuario']:
        post.imagem = imagem_upload
        post.titulo = titulo
        post.categoria = categoria_filtered
        post.conteudo = conteudo
        post.save()
        return redirect('/posts/home')
    
    
def comentario(request, id):

    comentario = request.POST.get('comentario')
    post = Post.objects.get(id=id)
    id_usuario = request.session.get('usuario')
    usuario = Usuario.objects.get(id=id_usuario)
    
    
    
    if len(comentario) < 10:
        return HttpResponse('opa')
    if len(comentario) > 100:
        return HttpResponse('carai')
    
    comentario = Comentario(comentario=comentario, post=post, usuario=usuario)
    comentario.save()
    return redirect(f'ver_post', id)