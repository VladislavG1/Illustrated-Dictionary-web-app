from django.shortcuts import render
from .models import Group

def catalog(request):
    data_group = Group.objects.all()
    context = {
        'title': "Содержание - Иллюстрированный словарь",
        'groups': data_group
    }
    return render(request, 'dictionary/catalog.html', context)

def word(request):
    context = {
        'title': "Слово - Иллюстрированный словарь"
    }
    return render(request, 'dictionary/word.html', context)