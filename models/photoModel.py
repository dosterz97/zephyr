import uuid
from django.db import models

class Photo(models.Model):
    photoId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    photoStorage = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)