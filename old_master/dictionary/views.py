from itertools import chain
from math import comb
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Group, Word, WordGroup
from django.db.models import Q

def catalog(request):
    # Обращение к таблицам Group и Word_Group через их модели и получение всех записей
    data_group = Group.objects.all()
    data_wordgroup = WordGroup.objects.all()

    # Переменные для полученных GET-запросов
    search = request.GET.get('search', None)
    capital_letters = request.GET.get('capital_letters', None)
    groups_filter = request.GET.get('groups_filter', None)

    # Алфавит для фильтра по заглавным буквам
    cyrillic = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", 
                "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ы", "э", "ю", "я"]

    # Если получен GET-запрос с заглавными буквами
    if capital_letters:
        # Преобразовываем в список полученную строку заглавных букв
        letters = list(capital_letters)
        filtered_words = [] # словарь для отфильтрованных слов
        # Цикл по всем буквам из GET-запроса
        for letter in letters:
            # Добавляем слово, начинающееся на нужную букву в словарь отфильтрованных слов
            filtered_words.extend(Word.objects.filter(Q(name__startswith=letter) | Q(name__startswith=letter.lower())))
        
        # Фильтр список по словам, которые совпадают с отфильтрованными словами
        data_wordgroup = data_wordgroup.filter(word__in=filtered_words)
    
    # Если получен GET-запрос с поисковым запросом
    if search:
        # Фильтруем список по словам, которые содержат текст поискового запроса
        data_wordgroup = data_wordgroup.filter(word__name__icontains=search)

    # Если получен GET-запрос с тематическими группами
    if groups_filter:
        # Разделяем полученный запрос по запятым и добавляем в список
        groups_filter_list = groups_filter.split(',')
        # Пустой объект модели WordGroup для будущих отфильтрованных групп
        combined_qs = WordGroup.objects.none()
        # Цикл по полученным из GET-запроса группам
        for element in groups_filter_list:
            # Нужная группа
            filter_group = Group.objects.get(alias_name=element)
            # Добавляем нужную группу в объект отфильтрованных групп
            combined_qs = combined_qs.union(data_wordgroup.filter(group=filter_group))

        # Фильтруем список по словам, которые относятся к списку отфильтрованных групп
        data_wordgroup = combined_qs

    # Пагинация
    paginator = Paginator(data_wordgroup, 50)
    current_page = request.GET.get('page')

    try:
        wordgroup = paginator.page(current_page)
    except PageNotAnInteger:
        wordgroup = paginator.page(1)
    except EmptyPage:
        wordgroup = paginator.page(paginator.num_pages)

    # Формируем контекст, содержащий все полученные ранее данные и передаем его шаблону catalog.html
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

    first_letter = data_word.name[:1]

    context = {
        'title': "- Иллюстрированный словарь",
        'words': data_word,
        'wordgroup': data_wordgroup,
        'fl': first_letter
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
    return render(request, 'dictionary/group_old.html', context)