from django.db import models

# Create your models here.

class UnitKerja(models.Model):
    unit_kerja_id = models.AutoField(primary_key=True)
    nama_unit_kerja = models.CharField(max_length=255)

    class Meta:
        db_table = 'mapeg_unit_kerja'
    def __str__(self):
        return self.nama_unit_kerja

class SubUnitKerja(models.Model):
    sub_unit_kerja_id = models.AutoField(primary_key=True)
    nama_sub_unit_kerja = models.CharField(max_length=255)

    class Meta: 
        db_table = 'mapeg_subunit'


    def __str__(self):
        return self.nama_sub_unit_kerja
    

class UnitKerja_SubUnitKerja(models.Model):
    id = models.AutoField(primary_key=True)
    unit_kerja = models.ForeignKey(UnitKerja, on_delete=models.CASCADE)
    sub_unit_kerja = models.ForeignKey(SubUnitKerja, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mapeg_unit_kerja_subunit'
        unique_together = ('unit_kerja', 'sub_unit_kerja')

    def __str__(self):
        return f'{self.unit_kerja} - {self.sub_unit_kerja}'