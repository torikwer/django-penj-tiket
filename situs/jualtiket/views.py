from django.http import HttpResponse
from .models import Tiket
from django.template import loader

from django.shortcuts import render

# Create your views here.

def index (request):
    daftar_tiket = Tiket.objects.order_by('-tanggal')# [0:0] kalau mau dibatasi object yang akan muncul
    template = loader.get_template('jualtiket/index.html')
    context = {
        'daftar_tiket' : daftar_tiket,
        }
    return HttpResponse (template.render(context, request))    
