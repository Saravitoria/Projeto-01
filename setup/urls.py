"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from projetoFinal import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina, name='pagina'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.conteudo, name='conteudo'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('formulario/', views.formulario, name='formulario'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('resenha/', views.resenha, name='resenha'),
    path('resenha/remove/<int:id>', views.remove, name = 'remove'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)  
