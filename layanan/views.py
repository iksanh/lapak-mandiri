
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Layanan
from .forms import LayananForm

# Layanan Views
@login_required
def index(request):
    layanan = Layanan.objects.all()
    return render(request, 'list.html', {'layanan': layanan, })

def create(request):
    if request.method == 'POST':
        form = LayananForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('layanan_list')
    else:
        form = LayananForm()
    return render(request, 'form.html', {'form': form, 'module':'Tambah Layanan'})

def update(request, pk):
    layanan = get_object_or_404(Layanan, pk=pk)
    if request.method == 'POST':
        form = LayananForm(request.POST, instance=layanan)
        if form.is_valid():
            form.save()
            return redirect('layanan_list')
    else:
        form = LayananForm(instance=layanan)
    return render(request, 'form.html', {'form': form, 'module':'Update Layanan'})

def delete(request, pk):
    layanan = get_object_or_404(Layanan, pk=pk)
    if request.method == 'POST':
        layanan.delete()
        return redirect('layanan_list')
    return render(request, 'layanan_confirm_delete.html', {'layanan': layanan})

# You can replicate similar views for PersyaratanLayanan and PengajuanLayanan.
