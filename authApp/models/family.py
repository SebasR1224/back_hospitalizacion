from django.db import models
from .user import User

class Family(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relationship = models.CharField('Relationship', max_length=50, blank=False)