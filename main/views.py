from datetime import date, timedelta
from django.http import HttpResponse
from django.shortcuts import render

from .models import Word

def index(request):  
    word = Word.objects.order_by('?').first()

    context = {
        'title': "Иллюстрированный словарь",
        'word': word,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': "О нас - Иллюстрированный словарь"
    }
    return render(request, 'main/about.html', context)