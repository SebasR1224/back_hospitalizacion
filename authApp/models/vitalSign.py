from django.db import models
from .user import User

class VitalSign(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Name', max_length=100, blank=False)