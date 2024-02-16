from django.urls import path

from dictionary import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('word/', views.word, name='word')
]