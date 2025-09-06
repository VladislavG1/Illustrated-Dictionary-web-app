from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]