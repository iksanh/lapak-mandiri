from django import forms

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()



from .models import PegawaiKoordinatorSubstansi, Pegawai
from unit_kerja.models import  UnitKerja

class PegawaiKoordinatorSubstansiForm(forms.ModelForm):
    class Meta:
        model = PegawaiKoordinatorSubstansi
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'unit_kerja' in self.data:
            try:
                unit_kerja_id = int(self.data.get('unit_kerja'))
                self.fields['pegawai'].queryset = Pegawai.objects.filter(unit_kerja_id=unit_kerja_id).order_by('nama')
            except (ValueError, TypeError):
                pass  # Invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['pegawai'].queryset = self.instance.unit_kerja.pegawai_set.order_by('nama')
        else:
            self.fields['pegawai'].queryset = Pegawai.objects.none()
