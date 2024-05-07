from django.contrib import admin

from dictionary.models import Group, Word, WordGroup, TranscriptionList

from django import forms

admin.site.register(WordGroup)
admin.site.register(TranscriptionList)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'alias_name': ('name',)}

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    prepopulated_fields = {'alias_name': ('name',)}