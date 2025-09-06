from django.urls import path

from dictionarywebsite import settings
from django.conf.urls.static import static


from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('media/<path:file_path>', views.media_view, name='media_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
