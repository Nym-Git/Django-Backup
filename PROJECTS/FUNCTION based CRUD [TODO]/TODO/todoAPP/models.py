from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Instructions(models.Model):
  Complete = models.BooleanField(default=False)
  Text_M   = models.CharField(max_length=500)
  
  def __str__(self):
    return self.Text_M

     