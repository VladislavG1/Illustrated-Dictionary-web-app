from django.contrib import admin

from dictionary.models import Group, Word, WordGroup

admin.site.register(WordGroup)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'alias_name': ('name',)}

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    prepopulated_fields = {'alias_name': ('name',)}