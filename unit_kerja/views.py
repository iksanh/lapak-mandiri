from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import UnitKerja
from .forms import UnitKerjaForm

# Create your views here.


def index(request):
  unit_kerja = UnitKerja.objects.all()
  context =  {
    'unit_kerja'  :  unit_kerja
  }

  context["unit_kerja"] =  unit_kerja

  return render(request, 'unit_kerja/list.html', context)

def create(request):
  if request.method == 'POST': 
    form = UnitKerjaForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect('unit_kerja_index')
  else:
    form = UnitKerjaForm()  

  context = {
    'form' : form,
    'data_master' : True,
    'unit_kerja': True
  }
  return render(request, 'unit_kerja/forms.html', context )



def update(request, id):
  context = {}
  unit_kerja = get_object_or_404(UnitKerja, unit_kerja_id = id)

  form  = UnitKerjaForm(request.POST or None, instance= unit_kerja)

  if form.is_valid():
    form.save()
    return redirect('unit_kerja_index')
  
  context["form"] = form

  return render(request, "unit_kerja/forms.html", context)

def destroy(request, id):
  unit_kerja = get_object_or_404(UnitKerja, unit_kerja_id = id)
  unit_kerja.delete()

  messages.success(request, 'Unit Kerja has been successfully deleted.')

  return redirect('unit_kerja_index')
