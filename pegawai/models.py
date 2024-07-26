from django.db import models
from unit_kerja.models import UnitKerja, SubUnitKerja
from koordinator_substansi.models import KoordinatorSubstansi


class PangkatGolongan(models.Model):
    
    pangkat = models.CharField(max_length=255)
    golongan = models.CharField(max_length=255)

    class Meta:
        db_table = 'mapeg_pangkat_golongan'

    def __str__(self):
        return f'{self.pangkat} / {self.golongan}'
    
# Create your models here.
class Pegawai(models.Model):
    id=models.AutoField(primary_key=True)
    nip = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    pangkat_golongan = models.ForeignKey(PangkatGolongan, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    unit_kerja = models.ForeignKey(UnitKerja, on_delete=models.SET_NULL, null=True, blank=True)
    sub_unit_kerja = models.ForeignKey(SubUnitKerja, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    
    class Meta:
        db_table = 'mapeg_pegawai'

    def __str__(self):
        return self.nama
    
    def get_koordinator_substansi_names(self):
        return ", ".join([ks.nama for ks in self.koordinator_substansi.all()])

    get_koordinator_substansi_names.short_description = 'Koordinator Substansi'
    

class PegawaiKoordinatorSubstansi(models.Model):
    unit_kerja=models.ForeignKey(UnitKerja, on_delete=models.CASCADE, null=True)
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    koordinator_substansi = models.ForeignKey(KoordinatorSubstansi, on_delete=models.CASCADE)
    tmt = models.DateField()  # Example of additional field
    akhir = models.DateField(blank=True, null=True)
    status = models.BooleanField()
    # You can add more fields here as needed

    
    class Meta:
        db_table = 'mapeg_pegawai_koorsub'
        unique_together = ('pegawai', 'koordinator_substansi')  # Ensure unique pairings