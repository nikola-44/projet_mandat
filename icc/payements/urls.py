# Dorian Chatelain
from django.urls import path

from . import views

urlpatterns = [
    path('', views.CheckoutPageView.as_view(), name='checkout'),
    path('charge/', views.charge, name='charge')
]