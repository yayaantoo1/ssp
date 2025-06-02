from django.db import models

# Create your models here.

class Barang(models.Model):
    kdbrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=75)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gmb=models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nama