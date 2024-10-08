
from django.shortcuts import render, get_object_or_404, redirect
from .models import Layanan, PersyaratanLayanan, PengajuanLayanan
from .forms import LayananForm, PersayaratanLayananForm, PengajuanLayananForm

# Layanan Views
def index(request):
    persyaratan_layanan = PersyaratanLayanan.objects.all()
    return render(request, 'persyaratan/list.html', {'persyaratan_layanan': persyaratan_layanan})

def create(request):
    if request.method == 'POST':
        form = PersayaratanLayananForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persyaratan_list')
    else:
        form = PersayaratanLayananForm()
    return render(request, 'persyaratan/form.html', {'form': form})

def update(request, pk):
    layanan = get_object_or_404(PersyaratanLayanan, pk=pk)
    if request.method == 'POST':
        form = PersayaratanLayananForm(request.POST, instance=layanan)
        if form.is_valid():
            form.save()
            return redirect('persyaratan_list')
    else:
        form = LayananForm(instance=layanan)
    return render(request, 'persyaratan/form.html', {'form': form})

def delete(request, pk):
    layanan = get_object_or_404(Layanan, pk=pk)
    if request.method == 'POST':
        layanan.delete()
        return redirect('persayaratan_list')
    return render(request, 'layanan_confirm_delete.html', {'layanan': layanan})

# You can replicate similar views for PersyaratanLayanan and PengajuanLayanan.
