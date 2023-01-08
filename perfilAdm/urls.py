from . import views
from django.urls import path, include

urlpatterns = [
    path('login_adm/',  views.login_adm, name='login_adm'),
    path('validar_login/', views.validar_login, name='validar_login'),
    path('home_adm/', views.home, name='home_adm'),
]