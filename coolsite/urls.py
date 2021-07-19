from django.contrib import admin
from django.urls import path, include
from coolsite import views

urlpatterns = [
    path('', include('cameras.urls')),#включение всех путей
    path('admin/', admin.site.urls, name='admin'), #административная часть
]

handler404 = views.pageNotFound #Обработчик ошибки 404
