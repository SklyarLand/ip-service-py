from cv2 import cv2
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, StreamingHttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.views.decorators import gzip

from cameras.models import Camera
import threading
import requests


# Получить страницу со списком камер
def index(request):  # HttpResponse
    cameras = Camera.objects.all()
    return render(request, 'cameras/index.html', {'title': "Активные камеры", "cameras": cameras})


# получить страницу камеры
def get(request, id):  # HttpResponse
    camera = Camera.objects.filter(pk=id)
    if not camera:
        return HttpResponseNotFound('<h1>Камеры c таким идентификатором не существует</h1>')

    camera = camera[0]
    print(camera.updated_at)
    return render(request, 'cameras/camera.html', {'title': camera.name, 'camera': camera})


# начать стрим в отдельном потоке
def start_stream(request, id):
    camera_thread_name = f"stream {id}"
    for thread in threading.enumerate():
        if thread.name == camera_thread_name:
            return HttpResponse(content={'already starting'}, content_type='application/json')
    threading.Thread(target=stream, name=camera_thread_name, daemon=True).start()
    return HttpResponse(content={'start'}, content_type='application/json')


# закончить стрим в отдельном потоке
def end_stream(request, id):
    camera_thread_name = f"stream {id}"
    for thread in threading.enumerate():
        if thread.name == camera_thread_name:
            # thread._stop()
            return HttpResponse(content={'end'}, content_type='application/json')
    return HttpResponse(content={'not end'}, content_type='application/json')


def stream():
    stream = requests.get('http://192.168.1.20:81/stream', stream=True)
    bytez = ''
    print(stream.headers)
    # while True:
    #    print(stream.raw.read(16384))
    #
    # bytez = ''
    # while True:
    #     print(stream.raw.read(16384))
    # camera = Cameras.objects.get(id=id)
    # print(f"http://{camera.ip_address}:{camera.port}/stream")
    # cap = cv2.VideoCapture(f"http://{camera.ip_address}:{camera.port}/stream")
    # print(cap)
    # ret, frame = cap.read()
    # response.content = frame
    # print(ret)
    # print(frame)
    # response.headers = {"Content-Type": 'multipart/x-mixed-replace;boundary=12345678900000000000098765432'}


# получить стрим
def get_stream():
    return HttpResponse()


# вывести список с потоками
def streams(request):
    threads = []
    for thread in threading.enumerate():
        threads.append({'name': thread.name, 'ident': thread.ident, 'daemon': thread.daemon})
    return JsonResponse(threads, safe=False)


def stream_gray_scal(request, id):
    return HttpResponse(id)


# получить стрим по другому
@gzip.gzip_page
def test(request, id):
    camera = Camera.objects.filter(pk=id)
    if not camera:
        return HttpResponseNotFound('<h1>Камеры c таким идентификатором не существует</h1>')

    camera = camera[0]
    try:
        return StreamingHttpResponse(camera.getStream(), content_type="multipart/x-mixed-replace;boundary=123456789000000000000987654321")
    except HttpResponseServerError as e:
        print("aborted")

