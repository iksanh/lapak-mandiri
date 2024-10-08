from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import UnitKerja, SubUnitKerja
from .forms import SubUnitKerjaForm

# Create your views here.


def index(request):
  sub_unit = SubUnitKerja.objects.all()
  context =  {
    'sub_unit_kerja'  :  sub_unit
  }

  return render(request, 'unit_kerja/sub/list.html', context)

def create(request):
  if request.method == 'POST': 
    form = SubUnitKerjaForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect('sub_unit_kerja_index')
  else:
    form = SubUnitKerjaForm()  

  context = {
    'form' : form,
    'data_master' : True,
    'sub_unit_kerja': True
  }
  return render(request, 'unit_kerja/sub/forms.html', context )



def update(request, id):
  context = {}
  sub_unit_kerja = get_object_or_404(SubUnitKerja, sub_unit_kerja_id = id)

  form  = SubUnitKerjaForm(request.POST or None, instance= sub_unit_kerja)

  if form.is_valid():
    form.save()
    return redirect('sub_unit_kerja_index')
  
  context["form"] = form

  return render(request, "unit_kerja/sub/forms.html", context)

def destroy(request, id):
  sub_unit_kerja = get_object_or_404(SubUnitKerja, sub_unit_kerja_id = id)
  sub_unit_kerja.delete()

  messages.success(request, 'Sub Unit Kerja telah dihapus.')

  return redirect('sub_unit_kerja_index')
