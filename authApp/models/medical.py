from django.db import models
from .user import User

class Medical(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField('Specialty', max_length=100, blank=False)
    registration = models.CharField('Registration', max_length=255, blank=False)