from django import forms


class TiketForm(forms.Form):
    deskripsi = forms.TextField(
        max_length = 2000,
        widget = forms.Textarea(
            attrs={
                'cols': 80,
                'rows': 20}))
#    class Meta:
#        model = Tiket
#        fields = ('nama_film',
#                  'jumlah_tiket',
#                  'deskripsi',
#                  'tanggal',
#                  'harga_satuan')
