# Generated by Django 2.0 on 2018-03-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jualtiket', '0005_posisi'),
    ]

    operations = [
        migrations.CreateModel(
            name='hargaSatuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harga', models.CharField(max_length=100)),
            ],
        ),
    ]
