from django import forms
from .models import Layanan, PersyaratanLayanan, PengajuanLayanan


class LayananForm(forms.ModelForm):
  persyaratan = forms.ModelMultipleChoiceField(
        queryset=PersyaratanLayanan.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
  class Meta:
    model = Layanan
    fields =['nama','persyaratan', 'waktu_mulai', 'waktu_selesai']

    widgets = {
      'nama': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
      'waktu_mulai': forms.DateTimeInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'type': 'datetime-local'}),
      'waktu_selesai': forms.DateTimeInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'type': 'datetime-local'}),
      
    }


class PersayaratanLayananForm(forms.ModelForm):
    class Meta:
        model = PersyaratanLayanan
        fields = ['deskripsi']
        widgets = {
            
            'deskripsi': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
        }

# class PengajuanLayananForm(forms.ModelForm):
#     class Meta:
#         model = PengajuanLayanan
#         fields = ['pegawai', 'layanan', 'file_persyaratan', 'status']
#         widgets = {
#             'pegawai': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 p-2'}),
#             'layanan': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
#             'status': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
      
#             'file_persyaratan': forms.ClearableFileInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
#         }


class PengajuanLayananForm(forms.ModelForm):
    class Meta:
        model = PengajuanLayanan
        fields = ['pegawai', 'layanan']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'layanan' in self.data:
            try:
                layanan_id = int(self.data.get('layanan'))
                layanan = Layanan.objects.get(id=layanan_id)
                persyaratan_list = layanan.persyaratan.all()
                for persyaratan in persyaratan_list:
                    self.fields[f'file_{persyaratan.id}'] = forms.FileField(label=f"Upload {persyaratan.deskripsi[:30]}")
            except (ValueError, Layanan.DoesNotExist):
                pass


