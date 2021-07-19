from django.urls import path, include
from .views import *

cameras_pattern = ([
    path('', get, name="cameras"),
    path('start/', start_stream, name="start"),
    path('end/', end_stream, name="end"),
    path('stream/', get_stream, name="stream"),
    path('test/', test, name="test"),
    # path('stream/', stream, name="stream"),
    # path('gray/', stream_gray_scal, name="stream_grayscal")
])

urlpatterns = [
    path('', index, name="main"),
    path('streams/', streams, name="streams"),
    path('cameras/<int:id>/', include(cameras_pattern))
]
