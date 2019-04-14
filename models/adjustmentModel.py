import uuid
from django.db import models

class Adjustment(models.Model):
  controllerId  = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  state = models.BooleanField()
  brightness models.IntegerField()
  red = models.IntegerField()
  blue = models.IntegerField()
  green = models.IntegerField()
  time = models.DateTimeField(auto_now_add=True)