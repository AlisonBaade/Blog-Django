from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256
from . import views
from django.utils.timezone import timezone
from Postagem.models import Categoria, Post
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from django.db.models import F, Q


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

def home_adm(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.filter(id=request.session.get('usuario')).first()
        usuario_logado = usuario
        usuarios = Usuario.objects.all()
        qnt_usuarios = usuarios.count()
        status = request.GET.get('status')
        search = request.GET.get('search')
        if search:
            usuarios = Usuario.objects.filter(nome__icontains=search)

        if usuario.tipo == 'AD':
            return render(request, 'home_adm.html', {'status': status,
                                                     'usuarios': usuarios,
                                                     'qnt_usuarios': qnt_usuarios,
                                                     'usuario_logado': usuario_logado,})
        else:
            return redirect('/logout')

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
            usuario = Usuario(tipo='AD', nome=nome, senha=senha,
                              email=email, sexo_usuario=sexo)
            usuario.save()
            return redirect('/home_adm/?status=0')
        except:
            return redirect('/home_adm/?status=4')
    elif autor == 'AD':  # CADASTRO APENAS DENTRO DA ÁREA DE ADM
        try:
            senha = sha256(senha.encode()).hexdigest()
            usuario = Usuario(tipo='AD', nome=nome, senha=senha,
                              email=email, sexo_usuario=sexo)
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
    if request.session.get('usuario'):
        usuario = Usuario.objects.filter(id=request.session.get('usuario')).first()
        if usuario.tipo == 'AD':
            usuario_logado = usuario
            categorias = Categoria.objects.all()
            qnt_categoria = categorias.count()
            status = request.POST.get('status')
            search = request.GET.get('search')
            if search:
                categorias = Categoria.objects.filter(nome__icontains=search)
            
            return render(request, 'cad_categoria.html',
                          {'status': status,
                           'categorias': categorias,
                           'qnt_categoria': qnt_categoria,
                           'usuario_logado': usuario_logado,
                           'modal_exclusao' : {'modal' : 'nao',}    
                           }
                          )
        else:
            return redirect('/logout')
    
def req_exclusao (request, id):
    if request.session.get('usuario'):
        usuario = Usuario.objects.filter(id=request.session.get('usuario')).first()
        if usuario.tipo == 'AD':
            usuario_logado = usuario
            categorias = Categoria.objects.all()
            qnt_categoria = categorias.count()
            status = request.POST.get('status')
            search = request.GET.get('search')
            if search:
                categorias = Categoria.objects.filter(nome__icontains=search)
                
            return render(request, 'cad_categoria.html',
                            {'status': status,
                            'categorias': categorias,
                            'qnt_categoria': qnt_categoria,
                            'usuario_logado': usuario_logado,
                            'modal_exclusao' : {'modal' : 'sim',
                                                'id' : id}
                            }
                        )
        else:
            return redirect('/logout')

def gerar_relatorio(request):
    posts = Post.objects.annotate(
        nome_autor=F('autor__nome'),
        nome_categoria=F('categoria__nome')
    )
    
    cnv = canvas.Canvas("posts.pdf", pagesize=A4)
    cnv.setFont("Times-Roman",18)
    cnv.drawString(210,800, 'Relatório de Postagens')
    pos_x = 60
    pos_y = 750

    for post in posts:
        cnv.setFont("Times-Roman", 10)
        cnv.drawString(pos_x,pos_y, post.titulo)
        pos_y -= 25
        cnv.drawString(pos_x, pos_y, post.nome_autor)
        pos_y -= 25
        cnv.drawString(pos_x,pos_y, post.nome_categoria)
        pos_y -= 40
        
        if pos_y <= 150:
            cnv.showPage()
            cnv.setFont("Times-Roman",18)
            cnv.drawString(210,800, 'Relatório de Postagens')
            pos_y = 750
              
    cnv.save()
    return redirect('/home_adm')