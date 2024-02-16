from django.shortcuts import render

def catalog(request):
    context = {
        'title': "Содержание - Илюстрированный словарь",
        'groups': [
            {
                "id": 1,
                "name": "Вопросы",
                "alias_name": "questions",
            },
            {
                "id": 2,
                "name": "Время",
                "alias_name": "time",
            },
            {
                "id": 3,
                "name": "Город",
                "alias_name": "city",
            },
            {
                "id": 4,
                "name": "Одежда",
                "alias_name": "clothes",
            },
            {
                "id": 5,
                "name": "Дом",
                "alias_name": "house",
            },
        ],
    }
    return render(request, 'dictionary/catalog.html', context)

def word(request):
    context = {
        'title': "Слово - Илюстрированный словарь"
    }
    return render(request, 'dictionary/word.html', context)