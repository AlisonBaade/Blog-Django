from . import views
from django.urls import path

urlpatterns= [
    path('home/', views.home, name='home'), 
    path('index/', views.index, name='index'), 
    path('ver_post/<int:id>', views.ver_post, name='ver_post'), 
    path('cadastro_post/', views.cadastro_post, name='cadastro_post'), 
]