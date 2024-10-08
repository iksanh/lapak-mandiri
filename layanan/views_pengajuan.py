
from django.shortcuts import render, get_object_or_404, redirect
from .models import Layanan, PersyaratanLayanan, PengajuanLayanan, PengajuanLayananFile
from .forms import LayananForm, PersayaratanLayananForm, PengajuanLayananForm
from mapeg.utils import encrypt_id, decrypt_id

# Layanan Views
def index(request):
    pengajuan_layanan = PengajuanLayanan.objects.all()
    daftar_layanan =  Layanan.objects.all()
    for lyn in daftar_layanan:
        lyn.encrypted_id = encrypt_id(lyn.id)
    
    context  = {'pengajuan_layanan': pengajuan_layanan, ' ': daftar_layanan}
    # return render(request, 'pengajuan/list.html', context)
    
    return render(request, 'pengajuan/show.html', context)

# def create(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = PengajuanLayananForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('pengajuan_list')
#         else: 
#             print(request.POST)
#             print(form.errors)
#     else:
#         form = PengajuanLayananForm()
#     return render(request, 'pengajuan/form.html', {'form': form})

def create(request, encrypted_id):
    decrypted_id = decrypt_id(encrypted_id)
    
    obj = get_object_or_404(Layanan, id=decrypted_id)
    
    
    return render(request, 'pengajuan/form.html', {'object': obj})

def update(request, pk):
    layanan = get_object_or_404(PersyaratanLayanan, pk=pk)
    if request.method == 'POST':
        form = PersayaratanLayananForm(request.POST, instance=layanan)
        if form.is_valid():
            form.save()
            return redirect('pengajuan_list')
    else:
        form = LayananForm(instance=layanan)
    return render(request, 'pengajuan/form.html', {'form': form})

def delete(request, pk):
    layanan = get_object_or_404(Layanan, pk=pk)
    if request.method == 'POST':
        layanan.delete()
        return redirect('persayaratan_list')
    return render(request, 'layanan_confirm_delete.html', {'layanan': layanan})

# You can replicate similar views for PersyaratanLayanan and PengajuanLayanan.
