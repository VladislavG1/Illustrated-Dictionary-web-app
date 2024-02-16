from django.shortcuts import render

def catalog(request):
    context = {
        'title': "Содержание - Илюстрированный словарь"
    }
    return render(request, 'dictionary/catalog.html', context)

def word(request):
    context = {
        'title': "Слово - Илюстрированный словарь"
    }
    return render(request, 'dictionary/word.html', context)