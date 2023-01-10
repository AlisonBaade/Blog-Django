from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256
from . import views


def login(request):
    # if request.session.get('usuario'):
    #     return redirect('posts/home/')
    status_cadastro = request.GET.get('status_cadastro')
    status_login = request.GET.get('status_login')
    return render(request, 'login.html', {'status_cadastro': status_cadastro,
                                          'status_login': status_login, })


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email, senha=senha).first()
    tam_usuario = Usuario.objects.filter()

    if usuario.tipo == 'AU':
        if len(tam_usuario) == 0:
            return redirect('/?status_login=0')
        elif len(tam_usuario) > 0:
            request.session['usuario'] = tam_usuario[0].id
            return redirect('/posts/home/')
    elif usuario.tipo == 'CO':
        if len(tam_usuario) == 0:
            return redirect('/?status_login=0')
        elif len(tam_usuario) > 0:
            request.session['usuario'] = tam_usuario[0].id
            return redirect('/posts/index')
    elif usuario.tipo == "AD":
        if len(tam_usuario) == 0:
            return redirect('/login_adm/?status=1')
        elif len(tam_usuario) > 0:
            request.session['usuario'] = tam_usuario[0].id
            return redirect('/home_adm')


def valida_cadastro(request):

    autor = request.POST.get('autor')
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    # verificando se não há nenhum email igual ja cadastrado
    usuario = Usuario.objects.filter(email=email)

    if len(nome.strip()) == 0:
        return redirect('/?status_cadastro=1')

    if len(email.strip()) == 0:
        return redirect('/?status_cadastro=5')

    if len(senha) < 8:
        return redirect('/?status_cadastro=2')

    if len(usuario) > 0:
        return redirect('/?status_cadastro=3')

    if autor == 'on':
        try:
            # criptografando a senha do usuario
            senha = sha256(senha.encode()).hexdigest()
            usuario = Usuario(tipo='AU', nome=nome, senha=senha, email=email)
            usuario.save()

            return redirect('/?status_cadastro=0')
        except:
            return redirect('/?status_cadastro=4')
    else:
        try:
            # criptografando a senha do usuario
            senha = sha256(senha.encode()).hexdigest()
            usuario = Usuario(tipo='CO', nome=nome, senha=senha, email=email)
            usuario.save()

            return redirect('/?status_cadastro=0')
        except:
            return redirect('/?status_cadastro=4')


def logout(request):
    request.session.flush()
    return redirect('/')

######################## ADMINISTRADOR #######################


def home_adm(request):
    return render(request, 'home_adm.html')


def login_adm(request):
    if request.session.get('usuario'):
        return redirect('/home_adm')

    status = request.GET.get('status')
    return render(request, 'login_adm.html', {'status': status})

