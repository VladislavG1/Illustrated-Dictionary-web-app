from itertools import chain
from math import comb
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Group, Word, WordGroup
from django.db.models import Q

def catalog(request):
    data_group = Group.objects.all()
    data_wordgroup = WordGroup.objects.all()

    with_voice = request.GET.get('with_voice', None)
    prefix = request.GET.get('prefix', None)
    postfix = request.GET.get('postfix', None)
    search = request.GET.get('search', None)
    capital_letters = request.GET.get('capital_letters', None)
    groups_filter = request.GET.get('groups_filter', None)

    cyrillic = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ы", "э", "ю", "я"]


    if capital_letters:
        letters = list(capital_letters)
        filtered_words = []
        for letter in letters:
            filtered_words.extend(Word.objects.filter(Q(name__startswith=letter) | Q(name__startswith=letter.lower())))
        
        data_wordgroup = data_wordgroup.filter(word__in=filtered_words)
    
    if with_voice:
        data_wordgroup = data_wordgroup.filter(~Q(word__audio=''))

    if prefix:
        data_wordgroup = data_wordgroup.filter(word__name__startswith=prefix)

    if postfix:
        data_wordgroup = data_wordgroup.filter(word__name__endswith=postfix)
    
    if search:
        data_wordgroup = data_wordgroup.filter(word__name__icontains=search)

    if groups_filter:
        groups_filter_list = groups_filter.split(',')
        # querysets = []
        combined_qs = WordGroup.objects.none()
        for element in groups_filter_list:
            filter_group = Group.objects.get(alias_name=element)
            # querysets.append(data_wordgroup.filter(group=filter_group))
            combined_qs = combined_qs.union(data_wordgroup.filter(group=filter_group))

        # data_wordgroup = list(chain(*querysets))
        data_wordgroup = combined_qs

    paginator = Paginator(data_wordgroup, 3)
    current_page = request.GET.get('page')

    try:
        wordgroup = paginator.page(current_page)
    except PageNotAnInteger:
        wordgroup = paginator.page(1)
    except EmptyPage:
        wordgroup = paginator.page(paginator.num_pages)

    context = {
        'title': "Содержание - Иллюстрированный словарь",
        'wordgroup': wordgroup,
        'groups': data_group,
        'alphabet': cyrillic,
        'dwg': data_wordgroup,
    }
    return render(request, 'dictionary/catalog.html', context)

def word(request, word_slug):
    
    data_word = Word.objects.get(alias_name=word_slug)
    data_wordgroup = WordGroup.objects.all()

    context = {
        'title': "- Иллюстрированный словарь",
        'words': data_word,
        'wordgroup': data_wordgroup
    }
    return render(request, 'dictionary/word.html', context)

def group(request, group_slug):

    data_group = Group.objects.get(alias_name=group_slug)
    data_wordgroup = WordGroup.objects.filter(group=data_group)

    with_voice = request.GET.get('with_voice', None)
    prefix = request.GET.get('prefix', None)
    postfix = request.GET.get('postfix', None)
    search = request.GET.get('search', None)
    capital_letters = request.GET.get('capital_letters', None)

    cyrillic = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ы", "э", "ю", "я"]


    if capital_letters:
        letters = list(capital_letters)
        filtered_words = []
        for letter in letters:
            filtered_words.extend(Word.objects.filter(Q(name__startswith=letter) | Q(name__startswith=letter.lower())))
        
        data_wordgroup = data_wordgroup.filter(word__in=filtered_words)
    
    if with_voice:
        data_wordgroup = data_wordgroup.filter(~Q(word__audio=''))

    if prefix:
        data_wordgroup = data_wordgroup.filter(word__name__startswith=prefix)

    if postfix:
        data_wordgroup = data_wordgroup.filter(word__name__endswith=postfix)
    
    if search:
        data_wordgroup = data_wordgroup.filter(word__name__icontains=search)

    paginator = Paginator(data_wordgroup, 3)
    current_page = request.GET.get('page')

    try:
        wordgroup = paginator.page(current_page)
    except PageNotAnInteger:
        wordgroup = paginator.page(1)
    except EmptyPage:
        wordgroup = paginator.page(paginator.num_pages)

    context = {
        'title': "- Иллюстрированный словарь",
        'group': data_group,
        'wordgroup': wordgroup,
        'slug_url': group_slug,
        'alphabet': cyrillic
    }
    return render(request, 'dictionary/group.html', context)