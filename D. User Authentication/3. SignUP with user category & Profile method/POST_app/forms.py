from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from django.contrib.admin.widgets import AdminDateWidget


CHOICES= [
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
    ]

choice_list = [
    ('Mental Health', 'Mental Health'),
    ('Heart Disease', 'Heart Disease'),
    ('Covid19', 'Covid19'),
    ('Immunization', 'Immunization'),
]


# post CreationFORM
class postFORMS(forms.Form):
  title = forms.CharField(max_length=500,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  summary = forms.CharField(max_length=50000,
    widget= forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  content = forms.CharField(max_length=50000,
    widget= forms.Textarea(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  category = forms.ChoiceField(choices=choice_list, 
    widget= forms.Select(attrs={
      'class':'form-control',
      'id'   :'title',      
    }))

  image = forms.FileField(
    widget=forms.ClearableFileInput(attrs={
      'placeholder': 'Thumbnail',
      'type':'file', 
      'id' : 'files', 
    }))


class BookingFORMS(forms.Form):
  Required_speciality = forms.CharField(max_length=500,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  Date_of_Appointment = forms.DateField(help_text='Required. Format: YYYY-MM-DD',
    widget=forms.TextInput(attrs={
      'placeholder': 'YYYY-MM-DD',
    }))

  Start_Time_of_Appointment = forms.CharField(help_text='Required. Format: YYYY-MM-DD',
    widget=forms.TextInput(attrs={
      'placeholder': 'Hours:minute',
    }))


class SignUpForm(UserCreationForm):
    
  profile_PIC = forms.FileField(
    widget=forms.ClearableFileInput(attrs={
      'type':'file', 
      'id' : 'files',  
      'multiple': True
    }))
  
  Category= forms.CharField(label='What is your are?', widget=forms.RadioSelect(choices=CHOICES))

  address = forms.CharField(max_length=500,
    widget=forms.Textarea(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  city = forms.CharField(max_length=500,
      widget=forms.TextInput(attrs={
        'type' :'text',
        'class':'form-control',
        'id'   :'title'
      }))

  state = forms.CharField(max_length=500,
      widget=forms.TextInput(attrs={
        'type' :'text',
        'class':'form-control',
        'id'   :'title'
      }))


  pincode = forms.CharField(max_length=500,
      widget=forms.TextInput(attrs={
        'type' :'text',
        'class':'form-control',
        'id'   :'title'
      }))

  class Meta:
    model = User
    fields = ('username','email','first_name','last_name', 'profile_PIC', 'Category', 'address','city','state','pincode','password1', 'password2', )
