from django.shortcuts import render
from .models import Group

def catalog(request):
    data_group = Group.objects.all()
    context = {
        'title': "Содержание - Илюстрированный словарь",
        'groups': data_group
    }
    return render(request, 'dictionary/catalog.html', context)

def word(request):
    context = {
        'title': "Слово - Илюстрированный словарь"
    }
    return render(request, 'dictionary/word.html', context)