from django.shortcuts import render, redirect
from .models import Instruction
from .forms import InstructionFORMS
from .import urls

# Create your views here.
def indexVIEW(request):
  if request.method == 'POST':
    form = InstructionFORMS(request.POST)
    
    if form.is_valid():
      new_req = Instruction(Text_M=request.POST['TextF'])
      new_req.save()
      return redirect('index')

  else:
    form = InstructionFORMS()

  context = {'form': form}
  return render(request,'index.html',context)
      


