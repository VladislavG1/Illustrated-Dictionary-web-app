from django.contrib import admin

from dictionary.models import Group, Word, WordGroup

admin.site.register(Group)
admin.site.register(Word)
admin.site.register(WordGroup)