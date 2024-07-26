from django.db import models
from unit_kerja.models import SubUnitKerja
# from pegawai.models import Pegawai
# Create your models here.

class KoordinatorSubstansi(models.Model):
    koorsub_id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    sub_unit_kerja = models.ForeignKey(SubUnitKerja, on_delete=models.CASCADE, null=True, default=None)
    

    
    def __str__(self):
        return f'{self.nama} - {self.sub_unit_kerja.nama_sub_unit_kerja}'