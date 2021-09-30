#Dorian Châtelain
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'produits'

urlpatterns = [
    path('', views.home, name='home'),
    path('gererProduits/', views.gererProduit, name='gererProduit'),
]
