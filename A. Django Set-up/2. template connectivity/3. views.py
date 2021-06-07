from django.shortcuts import render

# Create your views here.
def indexVIEW(request):
  return render(request,'index.html')
