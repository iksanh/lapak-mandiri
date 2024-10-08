from django.db import models
from pegawai.models import Pegawai

class Layanan(models.Model):
    nama = models.CharField(max_length=100)
    waktu_mulai = models.DateTimeField(null=True, blank=True)  # Start date and time
    waktu_selesai = models.DateTimeField(null=True, blank=True)  # End date and time
    # deskripsi = models.TextField(blank=True)
    persyaratan = models.ManyToManyField('PersyaratanLayanan', related_name='layanans', blank=True)

    def __str__(self) -> str:
        return self.nama

    class Meta:
        db_table = 'mapeg_layanan'

class PersyaratanLayanan(models.Model):
    deskripsi = models.TextField()

    def __str__(self) -> str:
        return self.deskripsi[:30]
    
    class Meta:
        db_table = 'mapeg_persayaratan_layanan'
  

class PengajuanLayanan(models.Model):
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE, related_name='pengajuan')
    layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE, related_name='pengajuan')
    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Diajukan', 'Diajukan'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Diajukan')
    file_persyaratan = models.FileField(upload_to='pengajuan_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.pegawai.nama} - {self.layanan.nama} ({self.status})"
    

    class Meta:
        db_table = 'mapeg_pengajuan_layanan'


class PengajuanLayananFile(models.Model):
    pengajuan_layanan = models.ForeignKey(PengajuanLayanan, on_delete=models.CASCADE, related_name='files')
    persyaratan = models.ForeignKey(PersyaratanLayanan, on_delete=models.CASCADE, related_name='pengajuan_files')
    file = models.FileField(upload_to='pengajuan_files/')

    def __str__(self):
        return f"{self.pengajuan_layanan} - {self.persyaratan.deskripsi[:30]}"
