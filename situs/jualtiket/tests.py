
import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Tiket

# Create your tests here.

class ModelTiketTes(TestCase):
    def tes(self):
        time = timezone.now() + datetime.timedelta(days=30)
        tiket_baru = Tiket(tanggal = time)
        self.assertIs(tiket_baru.daftar_tiket(), False)
