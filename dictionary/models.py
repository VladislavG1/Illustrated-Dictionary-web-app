# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from django.core.files.storage import default_storage

from django.core.exceptions import ValidationError


class Group(models.Model):
    # Переменные, отражающие поля таблицы
    name = models.CharField(max_length=128, unique=True, verbose_name='Название группы')
    alias_name = models.CharField(max_length=128, unique=True, verbose_name='Кодовое обозначение для группы')
    icon = models.ImageField(upload_to='group_icons', verbose_name='Иконка')

    class Meta:
        managed = False
        db_table = 'group'
        verbose_name = 'Тематическая группа'
        verbose_name_plural = 'Тематические группы'

    # Строковое представление объекта модели
    def __str__(self):
        return f"{self.name} ({self.pk})"

class Word(models.Model):
    name = models.CharField(max_length=128, verbose_name='Слово')
    alias_name = models.CharField(max_length=128, unique=True, verbose_name='Кодовое обозначение для слова')
    transcription = models.CharField(max_length=128, blank=True, null=True, verbose_name='Транскрипция')
    example = models.TextField(blank=True, null=True, verbose_name="Пример")
    image = models.ImageField(upload_to='dictionary_images', blank=True, null=True, verbose_name='Изображение')
    audio = models.FileField(upload_to='words_audio', blank=True, null=True, verbose_name='Аудио')

    # Дополнительные поля для отображения заполненности в списке админ-панели
    @property
    def transcription_filled(self):
        return bool(self.transcription)
    @property
    def example_filled(self):
        return bool(self.example)
    @property
    def image_filled(self):
        return bool(self.image)
    @property
    def audio_filled(self):
        return bool(self.audio)

    class Meta:
        managed = False
        db_table = 'word'
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self) -> str:
        return f"{self.name} ({self.pk})"
    
    
    def is_audio(self):
        if self.audio:
            return True
        elif default_storage.exists(self.audio.name):
            return True
        else:
            return False
        

class WordDay(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'word_day'
        unique_together = (('word', 'date'),)

class WordGroup(models.Model):
    
    word = models.ForeignKey(Word, on_delete=models.CASCADE, verbose_name='Слово')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Тематическая группа')

    class Meta:
        managed = False
        db_table = 'word_group'
        verbose_name = 'Связь между группами и словами'
        verbose_name_plural = 'Связи между группами и словами'
        unique_together = (('word', 'group'),)
    
    def __str__(self):
        return f"{self.group.name} - {self.word.name} ({self.pk})"
    
class Cyrillic(models.Model):
    character = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cyrillic'

    def __str__(self):
        return f"{self.character}"

class TranscriptionList(models.Model):
    letter = models.ForeignKey(Cyrillic, models.DO_NOTHING, verbose_name='Буква')
    word = models.ForeignKey(Word, on_delete=models.CASCADE, verbose_name='Слово')

    class Meta:
        managed = False
        db_table = 'transcription_list'
        verbose_name = 'Элемент списка транскрипций'
        verbose_name_plural = 'Элементы списка транскрипций'
        unique_together = (('letter', 'word'),)
    
    def __str__(self):
        return f"{self.letter} - {self.word.name}"