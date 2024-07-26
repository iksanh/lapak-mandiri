# pegawai_app/views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count
from .models import Pegawai

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