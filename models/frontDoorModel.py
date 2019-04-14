import uuid
from django.db import models

class FrontDoor(models.Model):
    status = models.IntegerField(primary_key = True)
    cameraId  = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)