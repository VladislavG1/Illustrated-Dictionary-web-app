from django.http import HttpResponse
from django.shortcuts import render

def index(request):  
    context = {
        'title': "Илюстрированный словарь"
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': "О нас - Илюстрированный словарь"
    }
    return render(request, 'main/about.html', context)