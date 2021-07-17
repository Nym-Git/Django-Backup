if request.method == "POST":
    name = request.POST.get("filename")
    myfile = request.FILES.getlist("uploadfoles")
        
    # multiple video storage
    for f in myfile:
      UploadClassVideos(f_name=name,myfiles=f).save()
    return HttpResponseRedirect(reverse('tclass', args=[str(id)])) 

  return render(request, 'class.html',{'videos':videos, 'local': card})
  
