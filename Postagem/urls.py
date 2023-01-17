from . import views
from django.urls import path

urlpatterns= [
    path('home/', views.home, name='home'), 
    path('index/', views.index, name='index'), 
    path('ver_post/<int:id>', views.ver_post, name='ver_post'), 
    path('cadastro_post/', views.cadastro_post, name='cadastro_post'), 
    path('edit_post/<int:id>', views.edit_post, name='edit_post'), 
    path('cadastrar_post/', views.cadastrar_post, name='cadastrar_post'), 
    path('excluir_post/<int:id>', views.excluir_post, name='excluir_post'), 
]