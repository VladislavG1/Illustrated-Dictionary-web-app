from datetime import date, timedelta
from django.http import HttpResponse
from django.shortcuts import render

from .models import Word, TranscriptionList

def index(request):  
    word = Word.objects.order_by('?').first()
    transcription_list = TranscriptionList.objects.all()

    cyrillic = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


    context = {
        'title': "Иллюстрированный словарь",
        'word': word,
        'alphabet': cyrillic,
        'list': transcription_list
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': "О нас - Иллюстрированный словарь"
    }
    return render(request, 'main/about_old.html', context)