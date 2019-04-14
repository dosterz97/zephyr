import uuid
from django.db import models

class TelevisionShow(models.Model):
    RESTRICTION_CHOICES = (
      ('0', 'NONE'),
      ('1', 'TV-PG'),
      ('1', 'TV-14'),
      ('2', 'TV-MA')
    )

    showName = models.CharField(primary_key = True)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now_add=True)
    ratingRestriction = models.CharField(choice = RESTRICTION_CHOICES, default = 0)