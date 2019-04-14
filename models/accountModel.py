import uuid
from django.db import models

class Account(models.Model):
  BASIC = 'Basic'
  ADVANCED = 'Advanced'
  ADMIN = 'Admin'

  PRIVILEGE_CHOICES = (
    (BASIC, 'Basic Access'),
    (ADVANCED, 'Advanced Access'),
    (ADMIN, 'Admin Access')
  )

  userId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  controllerId  = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
  firstName = models.CharField(max_length = 50)
  lastName = models.CharField(max_length = 50)
  privilege = models.CharField(
    choices = PRIVILEGE_CHOICES
    default = BASIC
  )
  created = models.DateTimeField(auto_now_add=True)