# Zumeri Faton et Châtelain Dorian
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'produits'

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('gererProduits/', views.gererProduit, name='gererProduit'),
    path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),
    path('<str:pk>/', views.modifier_produit, name='modifier_produit'),
    path('supprimer_produit/<str:pk>', views.supprimer_produit, name='supprimer_produit'),
]
