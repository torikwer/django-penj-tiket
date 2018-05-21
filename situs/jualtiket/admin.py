from django.contrib import admin
from jualtiket.models import TiketForm, posisi, Tiket


# posisi vertikal
class posisiInline(admin.TabularInline):
    model = posisi
    extra = 1

# tampilan
class formTiket(admin.ModelAdmin):
    fieldsets = [
        ('Masukkan Data',     {'fields': ('nama_film',
                                          'jumlah_tiket',
                                          'deskripsi',
                                          'tanggal',
                                          'harga_satuan',
                                          )
                               }
         ),
        ]
    inlines = [posisiInline]
    list_display = ('nama_film',
                    'jumlah_tiket',
                    'harga_satuan',
                    'tanggal')

    search_fields = ['nama_film']
    list_filter = ('tanggal',
                   'harga_satuan',
                   'jumlah_tiket')
admin.site.register(Tiket, formTiket)
