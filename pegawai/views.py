# pegawai_app/views.py
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Pegawai
from .forms import PegawaiForm
from unit_kerja.models import UnitKerja


#create 
@login_required
def pegawai_list(request):

    filter_kantor = request.GET.get('kantor')
    if filter_kantor : 
        pegawai_list = Pegawai.objects.filter(unit_kerja__nama_unit_kerja = filter_kantor)
    else: 
        pegawai_list = Pegawai.objects.all()

    paginator = Paginator(pegawai_list, 10) # show 10 record per page 

    page_number = request.GET.get('page')

    pegawai = paginator.get_page(page_number)

    kantor = UnitKerja.objects.all()

    context = {
        'pegawai' :pegawai,
        'title': 'Daftar Pegawai',
        'kantor': kantor,
        'kantor_value' : filter_kantor if filter_kantor else ''
    }



    return render(request, 'pegawai/pegawai_list.html', context)

def pegawai_create(request):
    form  = PegawaiForm()

    if request.method == 'POST':
        form = PegawaiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pegawai-list')
        
    context = {
        'form' : form,
        'title' : 'Buat Pegawai'
    }
    return render(request, 'pegawai/pegawai_form.html', {'form': form})



def pegawai_detail(request, pk):
    pegawai = get_object_or_404(Pegawai, pk=pk)
    context = {
        'pegawai' : pegawai,
        'title': 'deetail pegawai'
    }
    return render(request, 'pegawai/pegawai_detail.html', context)


# Update
def pegawai_update(request, pk):
    pegawai = get_object_or_404(Pegawai, pk=pk)
    if request.method == 'POST':
        form = PegawaiForm(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
            return redirect('pegawai_detail', pk=pegawai.pk)  # Redirect to the detail view after successful update
    else:
        form = PegawaiForm(instance=pegawai)
    return render(request, 'pegawai/pegawai_form.html', {'form': form})

# Delete
def pegawai_delete(request, pk):
    pegawai = get_object_or_404(Pegawai, pk=pk)
    if request.method == 'POST':
        pegawai.delete()
        return redirect('pegawai_list')  # Redirect to the list view after successful deletion
    return render(request, 'pegawai/pegawai_confirm_delete.html', {'pegawai': pegawai})



def pegawai_with_koordinator_view(request):
    # Get Pegawai instances with at least one related KoordinatorSubstansi
    pegawai_with_koordinator = Pegawai.objects.annotate(num_koordinator=Count('koordinator_substansi')).filter(num_koordinator__gt=0)
    
    # Pass the queryset to the template
    context = {
        'pegawai_list': pegawai_with_koordinator,
    }
    return render(request, 'pegawai/pegawai_with_koordinator.html', context)


def pegawai_by_unit_kerja(request):
    unit_kerja_id = request.GET.get('unit_kerja_id')
    if unit_kerja_id:
        pegawai = Pegawai.objects.filter(unit_kerja_id=unit_kerja_id).exclude(
            jabatan__icontains='kepala').values('id', 'nama')
    else:
        pegawai = Pegawai.objects.none()
    return JsonResponse(list(pegawai), safe=False)