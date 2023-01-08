from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('perfilUser.urls')),
    path('posts/', include('Postagem.urls')),
    path('admarea/', include('perfilAdm.urls')),
]
