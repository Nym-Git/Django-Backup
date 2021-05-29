from django import forms
from .models import Article
from ckeditor.fields import RichTextField


  
  #For Attribute ordering
class postFORMS(forms.ModelForm): 
  class Meta:
    model = Article
    fields = ('title','text','author')

    widgets = {  
      'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}), 
      'text':forms.TextInput(attrs={'class': 'form-control'}), 
      'author':forms.Select(attrs={'class': 'form-control'}), 
    }