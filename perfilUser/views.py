from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.session.get('usuario'):
        return redirect('home/')
    status_cadastro = request.GET.get('status_cadastro')
    status_login = request.GET.get('status_login')
    return render(request, 'login.html' , { 'status_cadastro': status_cadastro,
                                            'status_login': status_login,})


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario.objects.filter(email=email, senha=senha)
    
    if len(usuario) == 0:
        return redirect('/?status_login=0')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/home')


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
        autor = True
        try:
        # criptografando a senha do usuario
            senha = sha256(senha.encode()).hexdigest()
            usuario = Usuario(autor=autor, nome=nome, senha=senha, email=email)
            usuario.save()
            
            return redirect('/?status_cadastro=0')
        except:
            return redirect('/?status_cadastro=4')
    else:
        try:
        # criptografando a senha do usuario
            senha = sha256(senha.encode()).hexdigest()
            usuario = Usuario( nome=nome, senha=senha, email=email)
            usuario.save()
            
            return redirect('/?status_cadastro=0')
        except:
            return redirect('/?status_cadastro=4')
            
    





def logout(request):
    request.session.flush()
    return redirect('/')
