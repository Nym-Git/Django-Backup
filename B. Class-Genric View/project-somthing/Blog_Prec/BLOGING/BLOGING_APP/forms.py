from django import forms
from django.forms import ModelForm
from .models import PostCreation


  class postForm(ModelForm):
    model = PostCreation
    fields = '__all__'