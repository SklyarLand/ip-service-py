from django.http import HttpResponse
from django.http import HttpResponseNotFound


def index(request):  # HttpResponse
    return HttpResponse("<h1>Главная страница</h1>")


def pageNotFound(request, exception):  # HttpResponseNotFound
    return HttpResponseNotFound('<h1></h1>')
