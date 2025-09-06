from django.urls import path

from dictionarywebsite import settings
from dictionary import views

from django.conf.urls.static import static

app_name = 'dictionary'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('words/<slug:word_slug>/', views.word, name='word'),
    path('groups/<slug:group_slug>/', views.group, name='group'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)