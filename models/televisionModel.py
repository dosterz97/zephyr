import uuid
from django.db import models

class Television(models.Model):
    deviceId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField()