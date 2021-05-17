from django.db import models
from accounts.models import User


class Individual(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=8,blank=True)
    prefectures=models.CharField(max_length=40,blank=True)
    city=models.CharField(max_length=40,blank=True)
    address1=models.CharField(max_length=40,blank=True)
    address2=models.CharField(max_length=40,blank=True)

