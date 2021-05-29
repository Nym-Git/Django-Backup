from django.db import models


# Create your models here.
class NavigationField(models.Model):
  navName = models.CharField(max_length=30)
  Details = models.CharField(max_length=300)

  def __str__(self):
    return self.Details


class PostCreation(models.Model):
  post_Title = models.CharField(max_length=30)
  Details = models.CharField(max_length=300)

  def __str__(self):
    return self.post_Title