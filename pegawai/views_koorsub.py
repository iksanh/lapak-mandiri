# pegawai_app/views.py
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q


from .models import Pegawai, PangkatGolongan, PegawaiKoordinatorSubstansi
from unit_kerja.models import UnitKerja
from .forms import PegawaiKoordinatorSubstansiForm


#create 

def index(request):
    context =  {}

    #Get search paramaters from the request 

    search_unit_kerja = request.GET.get('unit_kerja', '')
    search_pegawai = request.GET.get('pegawai', '')
    search_status = request.GET.get('status', '')
    search_koorsub = request.GET.get('koordinator_substansi', '')

    #Build the query using Q object
    obj = PegawaiKoordinatorSubstansi.objects.all()

    if search_unit_kerja:
        obj = obj.filter(unit_kerja__unit_kerja_id=search_unit_kerja)

    if search_pegawai:
        obj = obj.filter(pegawai__nama__icontains=search_pegawai)

    # if search_status is not None:
    #     obj = obj.filter(status=search_status)

    if search_koorsub:
        obj = obj.filter(koordinator_substansi__nama__icontains=search_koorsub)

    #Order by unit_kerja and koordinator substansi

    obj = obj.order_by('unit_kerja', 'koordinator_substansi')


    paginator = Paginator(obj, 10)

    page_number = request.GET.get('page')

    koorsub = paginator.get_page(page_number)

    #fetch data Unit Kerja for search 
    unit_kerja_list=  UnitKerja.objects.all()
    

    context['koorsub']  = koorsub
    context['search_unit_kerja'] = search_unit_kerja
    context['search_pegawai'] = search_pegawai
    # context['search_status'] = search_status
    context['search_koorsub'] = search_koorsub
    context['unit_kerja_list'] = unit_kerja_list
    
    return render(request, 'pegawai/koorsub/list.html', context)

def create(request):
    context = {}
    form  = PegawaiKoordinatorSubstansiForm()

    if request.method == 'POST':
        form = PegawaiKoordinatorSubstansiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('koorsub_index')
        
    context["form"] = form
        
    return render(request, 'pegawai/koorsub/forms.html', context)



def detail(request, pk):
    obj = get_object_or_404(PangkatGolongan, pk=pk)
    context = {
        'pegawai' : obj
    }
    return render(request, 'pegawai/koorsub/detail.html', context)


# Update
def update(request, pk):
    context = {}
    obj = get_object_or_404(PegawaiKoordinatorSubstansi, pk=pk)
    if request.method == 'POST':
        form = PegawaiKoordinatorSubstansiForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('koorsub_index')  # Redirect to the detail view after successful update
    else:
        form = PegawaiKoordinatorSubstansiForm(instance=obj)

    context["form"] = form
    return render(request, 'pegawai/koorsub/forms.html', {'form': form})

# Delete
def delete(request, pk):
    obj = get_object_or_404(PangkatGolongan, pk=pk)
    obj.delete()
    
    return redirect('koorsub_index')  # Redirect to the list view after successful deletion
    


