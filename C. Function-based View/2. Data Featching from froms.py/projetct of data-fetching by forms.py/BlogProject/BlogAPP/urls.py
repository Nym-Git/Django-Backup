from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
from .views import UserRegisterView
from django.conf import settings


urlpatterns = [
  path('',views.indexVIEW, name='index'),
  path('display/',views.display, name='display'),
  path('details/<int:id>',views.detailsView, name='details'),  
  path('like/<int:id>',views.likeView, name='like'),
  path('register', UserRegisterView.as_view(), name='register'),
  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

