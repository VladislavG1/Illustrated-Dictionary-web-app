from django.shortcuts import render
from .models import Group, WordGroup

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

def group(request, group_slug):

    data_group = Group.objects.get(alias_name=group_slug)
    data_wordgroup = WordGroup.objects.all()

    context = {
        'title': "Тематическая группа - Иллюстрированный словарь",
        'group': data_group,
        'wordgroup': data_wordgroup
    }
    return render(request, 'dictionary/group.html', context)