from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from .models import Group, Word, WordGroup

def catalog(request):
    data_group = Group.objects.all()
    context = {
        'title': "Содержание - Иллюстрированный словарь",
        'groups': data_group
    }
    return render(request, 'dictionary/catalog.html', context)

def word(request, word_slug):
    
    data_word = Word.objects.get(alias_name=word_slug)
    data_wordgroup = WordGroup.objects.all()

    context = {
        'title': "Слово - Иллюстрированный словарь",
        'words': data_word,
        'wordgroup': data_wordgroup
    }
    return render(request, 'dictionary/word.html', context)

def group(request, group_slug):

    data_group = Group.objects.get(alias_name=group_slug)
    data_wordgroup = WordGroup.objects.filter(group=data_group)

    paginator = Paginator(data_wordgroup, 3)
    current_page = request.GET.get('page')

    try:
        wordgroup = paginator.page(current_page)
    except PageNotAnInteger:
        wordgroup = paginator.page(1)
    except EmptyPage:
        wordgroup = paginator.page(paginator.num_pages)

    context = {
        'title': "Тематическая группа - Иллюстрированный словарь",
        'group': data_group,
        'wordgroup': wordgroup
    }
    return render(request, 'dictionary/group.html', context)