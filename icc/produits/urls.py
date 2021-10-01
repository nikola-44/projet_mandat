#Dorian Châtelain
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'produits'

urlpatterns = [
    path('', views.home, name='home'),
    path('gererProduits/', views.gererProduit, name='gererProduit'),
    path('supprimer_produit/<str:pk>', views.supprimer_produit, name='supprimer_produit'),
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),

]
