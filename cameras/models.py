import requests
from django.db import models


class Camera(models.Model):
    name = models.CharField(max_length=250)
    ip_address = models.CharField(max_length=15)
    port = models.PositiveSmallIntegerField(default=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name} {self.pk}"

    def getStream(self):
        stream = requests.get(f"http://{self.ip_address}:{self.port}/stream", stream=True)

        for chunk in stream.iter_content(chunk_size=1024):
            print(chunk)
            yield (chunk)

            # yield (b'--frame\r\n'
            #       b'Content-Type: image/jpeg\r\n\r\n' + chunk + b'\r\n\r\n')
