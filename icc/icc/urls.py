"""icc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('contact/', views.contact, name='contact'),
    path('', views.accueil, name='accueil'),
    path('produits/', views.produits, name='produits'),
    path('accueilAdmin/', views.accueilAdmin, name='accueilAdmin'),
    path('reservations/', include('reservations.urls')),
    path('', views.acces),
    path('compte/', include('compte.urls')),
    path('contact/', include('contact.urls')),
    path('gererProduits/', views.gererProduits, name='gererProduit'),
    path('gererClient/', views.gererClients, name='gererClients'),
]

urlpatterns += staticfiles_urlpatterns()
