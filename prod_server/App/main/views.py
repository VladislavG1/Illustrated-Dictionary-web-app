import os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseNotFound
from django.conf import settings
from django.utils import timezone

from dictionary.models import Word, TranscriptionList, WordDay, WordGroup

def index(request):  
    # Обращение к текущей дате и запись ее в переменную today для модуля Слово дня
    today = timezone.now().date()

    # Обращение к таблице "Word_day" через модель WordDay, взятие значения поля date последней записи в переменную last_selected_date
    try:
        last_selected = WordDay.objects.latest('date')
        last_selected_date = last_selected.date
    except WordDay.DoesNotExist:
        last_selected_date = None

    # Обработка данных для модуля Слово дня
    # Если дата в последней записи таблицы БД "Word_day" не совпадает с текущей датой
    if last_selected_date != today:
        # Выбираем из модели Word случайное слово
        word = Word.objects.order_by('?').first()
        # Создаем запись в модели WordDay, передавая в нее выбранное слово и текущую дату
        WordDay.objects.create(word=word, date=today)
    else:
        # Иначе оставляем прежнее слово, содержащееся в последней записи модели WordDay
        word = WordDay.objects.latest('date').word

    stress = word.stress.split('_')
    stress = [int(item) for item in stress]
    word_split = list(word.name)
    for i in range(len(word_split)):
        if i in stress:
            word_split[i] += '&#x301;'
    word_name = "".join(word_split)

    # Обращаемся к таблице БД "Transcription_list" и получаем все записи
    transcription_list = TranscriptionList.objects.all()
    # Обращаемся к таблице БД "Word_group" и получаем все записи
    word_group = WordGroup.objects.all()

    # Массив с русским алфавитом для модуля Транскрипция
    cyrillic = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                 "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


    # Формируем контекст, содержащий все полученные ранее данные и передаем его шаблону index.html
    context = {
        'title': "Иллюстрированный словарь",
        'word': word,
        'word_name': word_name,
        'alphabet': cyrillic,
        'list': transcription_list,
        'wordgroup': word_group
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': "О нас - Иллюстрированный словарь"
    }
    return render(request, 'main/about_old.html', context)

def media_view(request, file_path):
    # Создаем абсолютный путь к файлу
    file_path = settings.MEDIA_ROOT + '/' + file_path

    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        return HttpResponseNotFound('<h1>Файл не найден</h1>')

    # Открываем файл в двоичном режиме чтения
    f = open(file_path, 'rb') 

    # Отправляем файл пользователю
    response = FileResponse(f)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
    return response