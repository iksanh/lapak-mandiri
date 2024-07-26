
import csv
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib import admin, messages

from django.http import JsonResponse
from .models import Pegawai, PangkatGolongan, PegawaiKoordinatorSubstansi
from unit_kerja.models import UnitKerja, SubUnitKerja
from .forms import CSVImportForm, PegawaiKoordinatorSubstansiForm
from .views import pegawai_with_koordinator_view

class PegawaiAdmin(admin.ModelAdmin):
    change_list_template = "admin/pegawai/pegawai_changelist.html"
    list_display = ('nip', 'nama', 'sub_unit_kerja',)
    search_fields = ('nip', 'nama', 'jabatan')
    list_filter = ('unit_kerja','sub_unit_kerja')
    list_per_page = 10

    # Define the admin action
    def import_csv(self, request):
        if request.method == "POST":
            form = CSVImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['csv_file']
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                for row in reader:
                    sub_unit_kerja, unit_kerja = row['unit_kerja_id'].split("-")
                    Pegawai.objects.update_or_create(
                        nip=row['nip'],
                        defaults={
                            'nama': row['nama'],
                            'pangkat_golongan': PangkatGolongan.objects.filter(golongan=row['pangkat_golongan']).first() ,
                            'jabatan': row['jabatan'],
                            'status': row['status'],
                            'unit_kerja_id': UnitKerja.objects.filter(NamaUnitKerja__icontains=unit_kerja.strip()).first().UnitKerjaID ,
                            'sub_unit_kerja_id':SubUnitKerja.objects.filter(NamaSubUnitKerja__icontains=sub_unit_kerja.strip()).first().SubUnitKerjaID,
                            
                        }
                    )
                self.message_user(request, "CSV file imported successfully.", messages.SUCCESS)
                return HttpResponseRedirect(request.get_full_path())
        else:
            form = CSVImportForm()
        return render(request, "admin/pegawai/csv_import_form.html", {"form": form})

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.admin_site.admin_view(self.import_csv), name='import-csv'),
            path('pegawai-with-koordinator/', self.admin_site.admin_view(pegawai_with_koordinator_view), name='pegawai_with_koordinator'),
        ]
        return custom_urls + urls
    
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_buttons'] = True
        return super().changelist_view(request, extra_context=extra_context)

    

admin.site.register(Pegawai, PegawaiAdmin)

class PegawaiKoorsubAdmin(admin.ModelAdmin):
    form = PegawaiKoordinatorSubstansiForm
    list_display = ('pegawai', 'koordinator_substansi', 'unit_kerja', 'tmt', 'akhir', 'status')
    search_fields = ('pegawai__nama', 'koordinator_substansi__nama', 'unit_kerja__nama')
    list_filter = ('unit_kerja', 'status')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('pegawaibyunitkerja/', self.admin_site.admin_view(self.pegawai_by_unit_kerja))
        ]
        return custom_urls + urls

    def pegawai_by_unit_kerja(self, request):
        unit_kerja_id = request.GET.get('unit_kerja_id')
        if unit_kerja_id:
            pegawai = Pegawai.objects.filter(unit_kerja_id=unit_kerja_id).values('id', 'nama')
        else:
            pegawai = Pegawai.objects.none()
        return JsonResponse(list(pegawai), safe=False)

# admin.site.register(Pegawai)
# admin.site.register(PangkatGolongan)




admin.site.register(PegawaiKoordinatorSubstansi, PegawaiKoorsubAdmin, )
