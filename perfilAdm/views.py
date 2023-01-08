from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UsuarioAdm
from hashlib import sha256
from . import views



def home(request):
    return render(request, 'home_adm.html')


def login_adm(request):
    if request.session.get('usuario'):
        return redirect('/admarea/home_adm.html')
    status = request.GET.get('status')
    return render(request,'login_adm.html', {'status': status})

    
    
def validar_login(request):
    
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    usuarios = UsuarioAdm.objects.filter(email = email, senha = senha)
    
    # VER DEPOIS SOBRE O FOR , SE EXCLUIR NÃO FUNCIONA
    for usuario in usuarios:
        pass
    ##################################################
    if len(usuarios) == 0:
        return redirect('/admarea/login_adm/?status=1')
    elif len(usuarios) > 0:
        if usuario.choice == 'M':
            request.session['usuarios'] = usuarios[0].id
            return redirect('/admarea/home_adm/')
        elif usuario.choice != 'M':
            return redirect('/admarea/login_adm/?status=2')
            
    

