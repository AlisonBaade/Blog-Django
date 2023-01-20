from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('valida_login/', views.valida_login, name='valida_login'),
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    path('logout/', views.logout, name='logout'),
    path('home_adm/', views.home_adm, name='home_adm'),
    path('cadastro_area_adm/', views.cadastro_area_adm, name='cadastro_area_adm'),
    path('cadastro_categoria/', views.cadastro_categoria, name='cadastro_categoria'),
    path('cad_categoria/', views.cad_categoria, name='cad_categoria'),
]
