from django.shortcuts import render


def accueil(request):
    return render(request, 'platforme/index.html')


def arquitetura(request):
    return render(request, 'platforme/arquitetura.html')
