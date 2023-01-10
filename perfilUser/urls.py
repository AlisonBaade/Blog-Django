from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'), 
    path('valida_login/', views.valida_login, name='valida_login'), 
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'), 
    path('logout/', views.logout, name='logout'),
    path('home_adm/', views.home_adm, name='home_adm'),
]
    
