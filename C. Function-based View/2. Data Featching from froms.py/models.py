from django.db import models

# Create your models here.
class Instruction(models.Model):
  Complete = models.BooleanField(default='False')
  Text_M    = models.CharField(max_length=500)

  def __str__(self):
    return self.Text_M