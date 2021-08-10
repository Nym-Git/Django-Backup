from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm, postFORMS, BookingFORMS
from .models import Post, Profile, AppointmentList
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from datetime import datetime, timedelta


def postVIEW(request):
  if request.method == 'POST':
    form = postFORMS(request.POST, request.FILES)
    if form.is_valid():
      new_req = Post(User_Name = request.user, Title=request.POST['title'], Summary=request.POST['summary'], Content=request.POST['content'],Category=request.POST['category'], Image=request.FILES['image'],)
      new_req.save()
      return HttpResponseRedirect(reverse('draft'))

  else:
    form = postFORMS()
  
  htmlcode = True
  context = {'form': form}
  return render(request,'post.html', context)


def draftVIEW(request):
  All_POSTS = Post.objects.all().filter(User_Name=request.user).order_by('-id')
  return render(request, 'draft.html', {'post': All_POSTS})


def homeDRVIEW(request):
  All_DR = Profile.objects.all().order_by('id')
  return render(request, 'home.html', {'All_DR': All_DR})


def mypostSVIEW(request):
  All_POST = Post.objects.all().filter(User_Name=request.user).order_by('-id')
  return render(request, 'accountPOST.html', {'posts': All_POST})


def listVIEW(request):
  All_POSTS = Post.objects.all().order_by('-id')
  return render(request, 'list.html', {'post': All_POSTS})


def detailsVIEW(request,id):
  POSTs_key = Post.objects.filter(id=id)
  return render(request, 'details.html', {'post': POSTs_key})


def bookingVIEW(request):
  point = AppointmentList.objects.all().order_by('-id').filter(User = request.user)
  return render(request, 'Bookinglist.html', {'point': point})



def bookVIEW(request,id):
  if request.method == 'POST':
    dr = Profile.objects.get(id=id)
    form = BookingFORMS(request.POST)

    if form.is_valid():
      now = ( datetime.now() ).strftime('%H:%M:%S')
      updated = ( datetime.now() + timedelta( minutes=45 )).strftime('%H:%M:%S')
      new_req = AppointmentList(User = request.user, DR = dr.user, Date =request.POST['Date_of_Appointment'],RequiredSpeciality =request.POST['Required_speciality'], start_time=now, end_time=updated)
      new_req.save()
      SCOPES = ['https://www.googleapis.com/auth/calendar']

      creds = None
      
      if os.path.exists('token.json'):
          creds = Credentials.from_authorized_user_file('token.json', SCOPES)
      # If there are no (valid) credentials available, let the user log in.
      if not creds or not creds.valid:
          if creds and creds.expired and creds.refresh_token:
              creds.refresh(Request())
          else:
              flow = InstalledAppFlow.from_client_secrets_file(
                  'client_secret.json', SCOPES)
              creds = flow.run_local_server(port=0)
          # Save the credentials for the next run
          with open('token.json', 'w') as token:
              token.write(creds.to_json())

      service = build('calendar', 'v3', credentials=creds)

      # Call the Calendar API
      now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
      print('Getting the upcoming 10 events')
      events_result = service.events().list(calendarId='944948457357-i06i9888hmpgksfcrnvj0qboa69lrjrp.apps.googleusercontent.com', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
      events = events_result.get('items', [])

      if not events:
          print('No upcoming events found.')
      for event in events:
          start = event['start'].get('dateTime', event['start'].get('date'))
          print(start, event['summary'])

      return HttpResponseRedirect(reverse('booking'))

  else:
    form = BookingFORMS()
  
  htmlcode = True
  context = {'form': form}
  return render(request,'book.html', context)


class updateVIEW(UpdateView):
  model = Post
  template_name = 'draftdetails.html'
  fields = ['Publised']
  success_url = reverse_lazy('list')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
          user = form.save()
          user.refresh_from_db()  # load the profile instance created by the signal request.FILES['Images']
          user.profile.profile_PIC = request.FILES['profile_PIC']
          user.profile.Full_Address = form.cleaned_data.get('address')
          user.profile.Category = form.cleaned_data.get('Category')
          user.profile.city = form.cleaned_data.get('city')
          user.profile.state = form.cleaned_data.get('state')
          user.profile.pincode = form.cleaned_data.get('pincode')
          user.save()
          raw_password = form.cleaned_data.get('password1')
          user = authenticate(username=user.username, password=raw_password)
          login(request, user)
          return HttpResponseRedirect(reverse('list'))
    else:
      form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
