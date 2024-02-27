from django.urls import path

from dictionary import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('words/<int:word_id>/', views.word, name='word'),
    path('groups/<slug:group_slug>/', views.group, name='group'),
]