import uuid
from django.db import models

class Light(models.Model):
    controllerId  = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    state = models.BooleanField()
    brightness models.IntegerField()
    red = models.IntegerField()
    blue = models.IntegerField()
    green = models.IntegerField()