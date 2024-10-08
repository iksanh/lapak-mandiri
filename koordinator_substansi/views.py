from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import KoordinatorSubstansi
from .forms import KoordinatorSubstansiForm

# Create your views here.


def index(request):
  koorsub = KoordinatorSubstansi.objects.all()

  context  = {
    'koorsub' : koorsub
  }

  return render(request, 'koordinator_substansi/list.html', context)

def create(request):

  if request.method == 'POST':
    form = KoordinatorSubstansiForm(request.POST)

    if form.is_valid():
      messages.success(request, 'Master data Koorsub berhasil ditambahkan')
      form.save()

      return redirect('koordinator_substansi_index')
  else:
    form = KoordinatorSubstansiForm()

  context = {
    'form': form
    
  }

  return render(request, 'koordinator_substansi/forms.html', context)


def update(request, id):
  context =  {}
  koorsub = get_object_or_404(KoordinatorSubstansi, koorsub_id = id)
  form = KoordinatorSubstansiForm(request.POST or None, instance=koorsub)

  if form.is_valid():
    form.save()
    messages.success(request, 'data koordintaor substansi berhasil di update')
    return redirect('koordinator_substansi_index')
  
  context["form"] = form
  return render(request, "koordinator_substansi/forms.html", context)


def destroy(request, id):
  koorsub = get_object_or_404(KoordinatorSubstansi, koorsub_id = id)

  koorsub.delete()

  messages.success(request, 'Koordinator Substansi berhasil dihapus')

  return redirect('koordinator_substansi_index')


  
      
  