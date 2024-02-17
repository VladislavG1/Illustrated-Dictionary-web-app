# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название группы')
    alias_name = models.CharField(max_length=128, verbose_name='Кодовое слово для группы')

    class Meta:
        managed = False
        db_table = 'group'
        verbose_name = 'Тематическая группа'
        verbose_name_plural = 'Тематические группы'

    def __str__(self):
        return f"{self.name} ({self.pk})"

class Word(models.Model):
    name = models.CharField(max_length=128, verbose_name='Слово')
    transcription = models.CharField(max_length=128, blank=True, null=True, verbose_name='Транскрипция')

    class Meta:
        managed = False
        db_table = 'word'
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self) -> str:
        return f"{self.name} ({self.pk})"


class WordGroup(models.Model):
    
    word = models.ForeignKey(Word, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'word_group'
        verbose_name = 'Связь между группами и словами'
        verbose_name_plural = 'Связи между группами и словами'
    
    def __str__(self):
        return f"{self.group.name} - {self.word.name} ({self.pk})"
    