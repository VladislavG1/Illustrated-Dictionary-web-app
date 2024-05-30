from django.contrib import admin
from django.contrib.admin.filters import FieldListFilter
from django.db.models import Q
from django.urls import reverse
from django.utils.html import mark_safe

from dictionary.models import Group, Word, WordGroup, TranscriptionList
from django import forms

admin.site.site_header = 'Панель управления'
admin.site.site_title = 'Панель управления'
admin.site.index_title = 'Главная страница'

class WordGroupInlineFormset(forms.BaseInlineFormSet):  
    def clean(self):
        super().clean()

        # Проверка, не пусты ли все инлайн-объекты
        all_groups_empty = all([not form.cleaned_data.get('group') for form in self.forms])
        if all_groups_empty:
            raise forms.ValidationError('Необходимо связать слово хотя бы с одной тематической группой.')
        
class TranscriptionInlineFormset(forms.BaseInlineFormSet):  
    def clean(self):
        super().clean()

        # Проверка, не пусто ли поле Транскрипция в случае добавления слова в список транскрипций
        for form in self.forms:
            if form.cleaned_data and not form.instance.word.transcription:
                raise forms.ValidationError('Поле Транскрипция не может быть пустым при добавлении элемента в список транскрипций.')

class WordGroupInline(admin.StackedInline):
    model = WordGroup
    formset = WordGroupInlineFormset
    extra = 0

class TranscriptionInline(admin.StackedInline):
    model = TranscriptionList
    formset = TranscriptionInlineFormset
    extra = 0

class WordGroupInlineFromGroup(admin.StackedInline):
    model = WordGroup
    extra = 0

class WordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Динамическое добавление поля выбора 'group' в форму
        if not self.instance.pk:
            self.fields['group'] = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    form = WordForm
    inlines = [WordGroupInline, TranscriptionInline]

    prepopulated_fields = {'alias_name': ('name',)}

    search_fields = ['name', 'pk']
    list_display = ('name', 'transcription_filled', 'example_filled', 'image_filled', 'audio_filled', 'id', 'view_on_site_link')
    list_filter = (
        ('transcription', admin.EmptyFieldListFilter),
        ('example', admin.EmptyFieldListFilter),
        ('image', admin.EmptyFieldListFilter),
        ('audio', admin.EmptyFieldListFilter),
    )

    def view_on_site_link(self, obj):
        url = reverse('dictionary:word', kwargs={'word_slug': obj.alias_name})
        return mark_safe(f'<a href="{url}" target="_blank"><img src="/static/admin/img/icon-viewlink.svg"></a>')
    view_on_site_link.short_description = 'Просмотр на сайте'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['view_on_site_link']
        return []

    # Изменение отображаемого имени поля с PK на ID
    def id(self, obj):
        return f"{obj.pk}"

    # Переопределение property-полей для отображения булевых значений в виде галочки/крестика
    def transcription_filled(self, obj):
        return bool(obj.transcription)
    transcription_filled.boolean = True
    transcription_filled.short_description = 'Транскрипция'
    def example_filled(self, obj):
        return bool(obj.example)
    example_filled.boolean = True
    example_filled.short_description = 'Пример'
    def image_filled(self, obj):
        return bool(obj.image)
    image_filled.boolean = True
    image_filled.short_description = 'Изображение'
    def audio_filled(self, obj):
        return bool(obj.audio)
    audio_filled.boolean = True
    audio_filled.short_description = 'Аудио'

    def save_model(self, request, obj, form, change):
        # Преобразование переноса строк в HTML-теги переноса строк
        if not '<br>' in obj.example:
            obj.example = obj.example.replace('\n', '<br>')

        # Сохранение объекта и удаление предыдущих файлов изображения и/или аудио, если они были изменены
        old_image = obj.image
        old_audio = obj.audio
        print('Saved')
        print(old_image)
        print(old_audio)
        super().save_model(request, obj, form, change)
        if old_image != obj.image:
            print('Deleted image')
            old_image.delete(save=False)
        if old_audio and old_audio != obj.audio:
            print('Deleted audio')
            old_audio.delete(save=False)


    def delete_model(self, request, obj):
        # Удаление объекта и связанных файлов
        obj.image.delete(save=False)
        obj.audio.delete(save=False)
        print('Object deleted')
        super().delete_model(request, obj)


admin.site.register(WordGroup)
admin.site.register(TranscriptionList)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [WordGroupInlineFromGroup]
    prepopulated_fields = {'alias_name': ('name',)}
    search_fields = ['name', 'pk']
    list_display = ('name', 'id')

    # Изменение отображаемого имени поля с PK на ID
    def id(self, obj):
        return f"{obj.pk}"