"""
Projeto...: iMoleculaX -
Móculo....: urls.py - 
Author....: Macedo, Glener Diniz - Engenheiro de Software Full Stack
dt-Incial.: 29 de Dezembro de 2025 - Última Alteração: 29 de Dezembro de 2025
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', lambda request: redirect('/usuarios/login/')),
    path('dashboard/', views.fnct_dashboard, name='url_dashboard'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('projetos/', include('projetos.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 🔧 Adiciona suporte a arquivos estáticos e mídia quando DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
