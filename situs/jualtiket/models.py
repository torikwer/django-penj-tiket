import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.

class Tiket(models.Model):
    nama_film = models.CharField(max_length=200)
    jumlah_tiket = models.PositiveIntegerField(default=0)
    deskripsi = models.TextField()
    tanggal = models.DateTimeField('tanggal')
    harga_satuan = models.CharField(max_length=7)
    def __str__(self):
        return self.nama_film
    def daftar_tiket(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.tanggal <= now

    deskripsi = models.CharField(max_length=2000,
                                 null = True)
    
class posisi(models.Model):
    posisi_duduk = (
        ('S', 'Semua Deret'),
        ('D', 'Depan'),
        ('T', 'Tengah'),
        ('B', 'Belakang'),
        )
    tiket = models.ForeignKey(Tiket,
                              blank = True,
                              null = True,
                              on_delete = models.CASCADE)
    deret_duduk = models.CharField(max_length=1,
                                   choices = posisi_duduk)
    def __str__(self):
        return self.deret_duduk

class TiketForm(ModelForm):
    class Meta:
        model = Tiket
        fields = ['nama_film',
                  'jumlah_tiket',
                  'deskripsi',
                  'tanggal',
                  'harga_satuan']

    
    
 
        
