# Châtelain Dorian
from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('gererSalon/', views.gererSalon, name='gererSalon'),
    # path('<str:pk>/', views.modifier_salon, name='modifier_salon'),

]