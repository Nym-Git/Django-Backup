from django.urls import path
from .import views

urlpatterns = [
    path('',views.indexVIEW, name='index'),
]
