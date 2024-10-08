# pegawai_app/views.py
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


from .models import Pegawai, PangkatGolongan
from .forms import PangkatGolonganForm


#create 

def index(request):
    context =  {}
    obj = PangkatGolongan.objects.all()

    context['pangkat_golongan']  = obj
    
    return render(request, 'pegawai/pangkat_golongan/list.html', context)

def create(request):
    context = {}
    form  = PangkatGolonganForm()

    if request.method == 'POST':
        form = PangkatGolonganForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pangkat_golongan_index')
        
    context["form"] = form
        
    return render(request, 'pegawai/pangkat_golongan/forms.html', context)



def detail(request, pk):
    obj = get_object_or_404(PangkatGolongan, pk=pk)
    context = {
        'pegawai' : obj
    }
    return render(request, 'pegawai/pangkat_golongan/pegawai_detail.html', context)


# Update
def update(request, pk):
    context = {}
    obj = get_object_or_404(PangkatGolongan, pk=pk)
    if request.method == 'POST':
        form = PangkatGolonganForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('pangkat_golongan_index')  # Redirect to the detail view after successful update
    else:
        form = PangkatGolonganForm(instance=obj)

    context["form"] = form
    return render(request, 'pegawai/pangkat_golongan/forms.html', {'form': form})

# Delete
def delete(request, pk):
    obj = get_object_or_404(PangkatGolongan, pk=pk)
    obj.delete()
    
    return redirect('pangkat_golongan_index')  # Redirect to the list view after successful deletion
    


