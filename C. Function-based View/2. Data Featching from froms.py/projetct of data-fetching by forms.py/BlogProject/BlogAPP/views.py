from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Instruction,Comment
from .forms import InstructionFORMS, commentFORMS, SignupFORMS
from .import urls
from django.views import generic 
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm



# Post Creation View
def indexVIEW(request):
  if request.method == 'POST':
    form = InstructionFORMS(request.POST, request.FILES)
    if form.is_valid():
      new_req = Instruction(User_Name = request.user,Title_M=request.POST['TitleF'],Details_M=request.POST['DetailsF'], ImagesM=request.FILES['Images'])  
      new_req.save()
      return HttpResponseRedirect('display')

  else:
    form = InstructionFORMS()

  context = {'form': form}
  return render(request,'index.html', context)



# Display the Posts-Data View
def display(request):
  All_POSTs = Instruction.objects.all()
  return render(request,'display.html', {'PostS':All_POSTs})



# Display Post-exactly-DATA with comments Display logic 
def detailsView(request, id):
  POSTs_key = Instruction.objects.filter(id=id)        # For display the unique Data  

  if request.method == 'POST':
    form = commentFORMS(request.POST)
    if form.is_valid():
      post_id_local_var = Instruction.objects.get(id=id)
      newReq = Comment(Comment=request.POST['CommentF'], User_Name = request.user, post_ID = post_id_local_var)  
      newReq.save()
      return HttpResponseRedirect(reverse('details', args=[str(id)]))     # For refrace the page

  else:
    form = commentFORMS()

  All_Comments = Comment.objects.order_by('-id').filter(post_ID=id)       # Filtering the command for Display on exact post
  return render(request,'detials.html', {'ID':POSTs_key , 'CommentS':All_Comments, 'forms': form}) 



#def TrendingCountView(request, id):
#  comments_count = Comment.objects.filter(post_ID = id).count()
#  All_POSTs = Instruction.objects.all().order_by('-comments_count')
#  return render(request,'trending.html', {'PostS':All_POSTs})


#comments_count = Comment.objects.filter(post=mypost).count()
# Post Comment View
#def commentView(request, id):
#  if request.method == 'POST':
#    form = commentFORMS(request.POST)
#    if form.is_valid():
#      newReq = Comment(Comment=request.POST['CommentF'], User_Name = request.user, post_ID =request.POST[id])  
#      newReq.save()
#      return HttpResponseRedirect('lol')

#  else:
#    form = commentFORMS()
#
#  context = {'forms': form}
#  return render(request,'details.html',context)

      

# Display Post-like
def likeView(request, id):
  post_ID = get_object_or_404(Post, id = request.POST.get('post_id'))
  Post_ID.Likes_M.add(request.user)
  return HttpResponseRedirect(post_ID.get_absolute_url())




# SignUP by class based view
class UserRegisterView(generic.CreateView):
  form_class = SignupFORMS
  template_name  = 'registration/register.html'
  success_url = reverse_lazy('login')