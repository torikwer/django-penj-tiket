# Generated by Django 2.0 on 2018-02-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jualtiket', '0008_auto_20180310_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posisi',
            name='deret_duduk',
            field=models.CharField(choices=[('S', 'Semua Deret'), ('D', 'Depan'), ('T', 'Tengah'), ('B', 'Belakang')], max_length=1),
        ),
        migrations.AlterField(
            model_name='tiket',
            name='jumlah_tiket',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
