from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# post CreationFORM
class InstructionFORMS(forms.Form):
  TitleF = forms.CharField(max_length=500,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  DetailsF= forms.CharField(max_length=50000,
    widget= forms.Textarea(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  Images= forms.FileField(
    widget=forms.ClearableFileInput(attrs={
      'type':'file', 
      'id' : 'files',  
      'multiple': True
    }))


# Comment form
class commentFORMS(forms.Form):
  CommentF = forms.CharField(max_length=500,
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))




# sign-up form based class based view 
class SignupFORMS(UserCreationForm):
  email = forms.EmailField(
    widget=forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  first_name= forms.CharField(
    widget= forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  last_name= forms.CharField(
    widget= forms.TextInput(attrs={
      'type' :'text',
      'class':'form-control',
      'id'   :'title'
    }))

  #For Attribute ordering
  class Meta:
    model = User
    fields = ('username','email','first_name','last_name','password1','password2')

  #For user-name and password designing
  def __init__(self, *args, **kwargs):
    super(SignupFORMS,self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control' 
    self.fields['password1'].widget.attrs['class'] = 'form-control' 
    self.fields['password2'].widget.attrs['class'] = 'form-control' 