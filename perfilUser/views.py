from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256
from . import views
from django.utils.timezone import timezone
from Postagem.models import Categoria


def login(request):
    if request.session.get('usuario'):
        return redirect('posts/home/')
    status_cadastro = request.GET.get('status_cadastro')
    status_login = request.GET.get('status_login')
    return render(request, 'login.html', {'status_cadastro': status_cadastro,
                                          'status_login': status_login, })


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email, senha=senha).first()

    
    if usuario:
        if usuario.tipo == "AU":
            request.session['usuario'] = usuario.id
            return redirect('/posts/home/')                    
        if usuario.tipo == 'CO':
            request.session['usuario'] = usuario.id
            return redirect('/posts/index')
        if usuario.tipo == 'AD':
            request.session['usuario'] = usuario.id
            return redirect('/home_adm')
    if not usuario:
        return redirect('/?status_login=0')
                


def valida_cadastro(request):

    autor = request.POST.get('autor')
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha_1 = request.POST.get('senha1')

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

    if senha != senha_1:
        return redirect('/?status_cadastro=6')

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
    usuarios = Usuario.objects.all()
    qnt_usuarios = usuarios.count()
    status = request.GET.get('status')
    return render(request, 'home_adm.html', {'status': status,
                                             'usuarios': usuarios,
                                             'qnt_usuarios': qnt_usuarios})


def cadastro_area_adm(request):

    autor = request.POST.get('autor')
    email = request.POST.get('email')
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    senha_1 = request.POST.get('senha1')
    sexo = request.POST.get('sexo')
    
    usuario = Usuario.objects.filter(email=email)

    if len(nome.strip()) == 0:
        return redirect('/home_adm/?status=1')

    if len(email.strip()) == 0:
        return redirect('/home_adm/?status=2')

    if len(senha) < 8:
        return redirect('/home_adm/?status=3')

    if len(usuario) > 0:
        return redirect('/home_adm/?status=4')

    if senha != senha_1:
        return redirect('/home_adm/?status=5')
    
    if autor == 'AU':
        try:
            senha = sha256(senha.encode()).hexdigest()
            usuario = Usuario(tipo='AD', nome=nome, senha=senha, email=email, sexo_usuario=sexo)
            usuario.save()
            return redirect('/home_adm/?status=0')
        except:
            return redirect('/home_adm/?status=4')
    elif autor == 'AD': # CADASTRO APENAS DENTRO DA ÁREA DE ADM
        try:
            senha = sha256(senha.encode()).hexdigest()
            usuario = Usuario(tipo='AD', nome=nome, senha=senha, email=email, sexo_usuario=sexo)
            usuario.save()

            return redirect('/home_adm/?status=0')
        except:
            return redirect('/home_adm/?status=4')


def cadastro_categoria(request):
    
    nome = request.POST.get('nome_categoria')
    categoria = Categoria.objects.filter(nome=nome)
    
    if len(nome.strip()) == 0:
        return redirect('/home_adm/?status=1')
    
    
    categoria = Categoria(nome=nome)
    categoria.save()
    return redirect('/cad_categoria/?status=0')
    
    
def cad_categoria(request):
    categorias = Categoria.objects.all()
    qnt_categoria = categorias.count()
    status = request.POST.get('status')
    return render(request, 'cad_categoria.html', {'status': status,
                                                  'categorias': categorias,
                                                  'qnt_categoria': qnt_categoria})   



