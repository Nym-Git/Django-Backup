from django.urls import path
from .import views

urlpatterns = [
  path('course/', views.course.as_view(), name='course'),  
  path('nav/', views.navigation.as_view(), name='navigation'), 
  path('post/', views.post, name='post'), 
]
