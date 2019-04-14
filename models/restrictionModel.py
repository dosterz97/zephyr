import uuid
from django.db import models

class Restriction(models.Model):
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'
    SUNDAY = 'SU'

    DAY_CHOICES = (
      (MONDAY, 'MONDAY'),
      (TUESDAY,'TUESDAY'),
      (WEDNESDAY,'WEDNESDAY'),
      (THURSDAY,'THURSDAY'),
      (FRIDAY,'FRIDAY'),
      (SATURDAY, 'SATURDAY'),
      (SUNDAY, 'SUNDAY')
    )


    RESTRICTION_CHOICES = (
      ('0', 'NONE'),
      ('1', 'TV-PG'),
      ('1', 'TV-14'),
      ('2', 'TV-MA')
    )

    restrictionId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    deviceId = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
    userId = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)

    dayOfWeek = models.CharField(choice = DAY_CHOICES)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now_add=True)
    ratingRestriction = models.CharField(choice = RESTRICTION_CHOICES, default = 0)