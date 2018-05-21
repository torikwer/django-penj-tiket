# Generated by Django 2.0 on 2018-03-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jualtiket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tanggal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_penerimaan', models.DateTimeField(verbose_name='tanggal ditentukan')),
            ],
        ),
        migrations.CreateModel(
            name='Tiket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_tiket', models.CharField(max_length=200)),
                ('jumlah_tiket', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
