from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.accueil, name="home"),
    path('evenements/', views.event, name="events"),
    path('suggestion/', views.contact, name="contact"),
    path('payer/', views.paiement,name="paiement"),
    path('liste/',views.listevents,name="listevents"),
    path('supprimer/<int:id>/', views.delete,name="supprimerE"),
]
