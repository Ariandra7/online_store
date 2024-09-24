from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
# urlpatterns = [...] - это список, который Django использует для маршрутизации URL-адресов.
# path('', views.post_list, name='post_list') - это маршрут, который сопоставляет URL-адрес '' 
# (пустой строка) с функцией post_list из модуля views.py.