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
    search = request.GET.get('search')

    if search:
        post = Post.objects.filter(autor=usuario, titulo__icontains=search)
    else:
        posts_paginator = Paginator(post, 10)
        page_num = request.GET.get('page')
        post = posts_paginator.get_page(page_num)

    if usuario.tipo == 'AU':
        return render(request, 'home.html',
                      {'usuario_logado': usuario_logado,
                       'usuario_autor': usuario,
                       'post': post,
                       'qnt_post': qnt_post,
                       'modal_exclusao': {'modal': 'nao'}
                       }
                      )
    else:
        return redirect('/logout')

def home_excluir(request, id):
    usuario_req = request.session.get('usuario')
    usuario = Usuario.objects.filter(id=usuario_req).first()
    usuario_logado = usuario
    post = Post.objects.filter(autor=usuario)
    qnt_post = post.count()
    search = request.GET.get('search')

    if search:
        post = Post.objects.filter(autor=usuario, titulo__icontains=search)
    else:
        posts_paginator = Paginator(post, 10)
        page_num = request.GET.get('page')
        post = posts_paginator.get_page(page_num)

    if usuario.tipo == 'AU':
        return render(request, 'home.html',
                      {'usuario_logado': usuario_logado,
                       'usuario_autor': usuario,
                       'post': post,
                       'qnt_post': qnt_post,
                       'modal_exclusao': {'modal': 'sim',
                                          'id': id}
                       }
                      )
    else:
        return redirect('/logout')

def index(request):
    if request.session.get('usuario'):
        categorias = Categoria.objects.all()
        posts = Post.objects.all()
        search = request.GET.get('search')

        if search:
            page = Post.objects.filter(titulo__icontains=search)
        else:
            posts_paginator = Paginator(posts, 10)
            page_num = request.GET.get('page')
            page = posts_paginator.get_page(page_num)

        usuario = Usuario.objects.filter(id=request.session.get('usuario')).first()
        usuario_logado = usuario
        if usuario.tipo == 'CO':
            return render(request, 'index.html', {'categorias': categorias,
                                                  'page': page,
                                                  'usuario_logado': usuario_logado,
                                                  'search': search, })
        else:
            return redirect('/logout')

def ver_post(request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.filter(id=request.session.get('usuario')).first()
        usuario_logado = usuario
        
        if usuario.tipo == 'CO':
            post = Post.objects.filter(id=id).first()
            comentarios = Comentario.objects.filter(post=id)
            status_comentario = request.GET.get('status_comentario')
            return render(request, 'ver_post.html', {'post': post,
                                                     'comentarios': comentarios,
                                                     'usuario_logado': usuario_logado,
                                                     'status_comentario': status_comentario})

def edit_post(request, id):
    if request.session.get('usuario'):
        post = Post.objects.filter(id=id).first()
        categorias = Categoria.objects.all()
        usuario_req = request.session.get('usuario')
        usuario = Usuario.objects.filter(id=usuario_req).first()
        if usuario.tipo == 'AU':
            usuario_logado = usuario
            return render(request, 'edit_post.html', {'post': post,
                                                      'categorias': categorias,
                                                      'usuario_logado': usuario_logado})

def cadastrar_post(request):
    # PÁGINA DE CADASTRO DE POSTAGEM
    if request.session.get('usuario'):
        usuario_req = request.session.get('usuario')
        usuario = Usuario.objects.filter(id=usuario_req).first()
        if usuario.tipo == 'AU':
            usuario_logado = usuario
            categorias = Categoria.objects.all()
            status = request.GET.get('status')
            return render(request, 'cadastrar_post.html', {'categorias': categorias,
                                                           'usuario_logado': usuario_logado,
                                                           'usuario_req': usuario_req,
                                                           'status': status})

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
        
        excluir = request.POST.get('excluir')
        nao_excluir = request.POST.get('nao_excluir')
        
        if excluir:
            Post.objects.filter(id=id).delete()
            return redirect('/posts/home')
        if nao_excluir:
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

    if len(comentario) > 100:
        return redirect('/posts/ver_post/' + str(id) + '?status_comentario=0')

    comentario = Comentario(comentario=comentario, post=post, usuario=usuario)
    comentario.save()
    return redirect(f'ver_post', id)

def excluir_categoria(request, id):
    if request.session.get('usuario'):

        excluir = request.POST.get('excluir')
        nao_excluir = request.POST.get('nao_excluir')

        if excluir:
            Categoria.objects.filter(id=id).delete()
            return redirect('/cad_categoria')
        if nao_excluir:
            return redirect('/cad_categoria')
