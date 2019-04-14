import uuid
from django.db import models

class Camera(models.Model):
    cameraId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    sensorId = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
    photoStorage = models.CharField(max_length = 50)
    recording = models.BooleanField()