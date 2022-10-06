from django.db import models
from .user import User


class Patient(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direction = models.CharField('Direction', max_length=100, blank = False)
    city = models.CharField('City', max_length=50, blank = False)
    dateOfBirth = models.DateField('dateOfBirth', blank = False)
    latitude = models.CharField('Latitude', max_length=50, blank = True)
    length =  models.CharField('Length', max_length=50, blank = True)
    family = models.ForeignKey(User, related_name= 'family_std', on_delete=models.CASCADE)
    medical = models.ForeignKey(User, related_name= 'medical_std', on_delete=models.CASCADE)