from . import views
from django.urls import path

urlpatterns= [
    path('home/', views.home, name='home'), 
    path('index/', views.index, name='index'), 
]