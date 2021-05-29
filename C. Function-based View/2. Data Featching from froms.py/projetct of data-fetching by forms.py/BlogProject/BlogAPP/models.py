from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# POST creation 
class Instruction(models.Model):
  User_Name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_Name')
  id = models.BigAutoField(primary_key=True)
  Title_M   = models.CharField(max_length=200,null=True,primary_key=False)
  Details_M = RichTextField(null=True)
  Likes_M = models.ManyToManyField(User, related_name='blog_Post')
  ImagesM  = models.FileField(blank=True, upload_to='images/')
  published_date = models.DateTimeField(default=timezone.now)
  
#  image    = models.ImageField(upload_to='images/',blank=True,null=True)
  
  def __str__(self):
    return self.Title_M 


# POST comment 
class Comment(models.Model):
  User_Name = models.ForeignKey(User, on_delete=models.CASCADE)
  post_ID   = models.ForeignKey(Instruction, on_delete=models.CASCADE,default=0)
  Comment = models.CharField(max_length=200,null=True)
  Commented_date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.Comment

    

# Google ADDS 
class Google_Add(models.Model):
  Compeny_Name = models.CharField(max_length=200,null=True)
  ADD  = models.FileField(blank=True, upload_to='Google_ADDs/')
  published_date = models.DateTimeField(default=timezone.now)
  Clicking = models.ManyToManyField(User, related_name='clicking')
  
  def __str__(self):
    return self.Compeny_Name
    


# Google ADDS 
class Category(models.Model):
  Category_Field = models.CharField(max_length=200,null=True)
  published_date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.Cetegory
    