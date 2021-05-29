from django.views.generic import TemplateView,ListView
from .models import NavigationField, PostCreation
from .forms import postForm
# Create your views here.

class navigation(ListView):
  model = NavigationField
  template_name = 'nav.html'


class course(TemplateView):
  template_name = 'cource.html'
  

def post(request):

	form = postForm()

	if request.method == 'POST':
		form = postForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'post.html', context)