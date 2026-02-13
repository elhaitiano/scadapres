from django.urls import path
from .views import accueil, arquitetura

urlpatterns = [
    path('', accueil, name='accueil'),
    path('arquitetura/', arquitetura, name='arquitetura'),
]
