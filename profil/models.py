from django.db import models

# Create your models here.


class Jenis(models.Model):
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama
    
    
class Barang(models.Model):
    kdbrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=75)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gmb=models.CharField(max_length=150, blank=True)
    waktu_post = models.DateTimeField(auto_now_add=True)
    jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama
    

# class About(models.Model):
#     judul = models.CharField(max_length=200)
#     isi = models.TextField()
#     img = models.ImageField(upload_to='', blank=True)
#     img2 = models.ImageField(upload_to='', blank=True)

#     def __str__(self):
#         return self.judul
    

#uas
    
#tentang
class About(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    
    instagram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.judul
    
#Portfolio
class Portofolio(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='portofolio/', blank=True, null=True)
    link_sumber = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.judul
    
#Hero 
class Hero(models.Model):
    salam_pembuka = models.CharField(max_length=100, default="Halo Semua 👋, saya")
    nama = models.CharField(max_length=100)
    profesi = models.CharField(max_length=200, help_text="Contoh: Lecturer & Content Creator")
    tagline = models.TextField()
    foto_profil = models.ImageField(upload_to='hero/')
    
    def __str__(self):
        return self.nama
#klient
class Client(models.Model):
    nama = models.CharField(max_length=100)
    # Anda akan mengunggah logo yang FULL COLOR di sini
    logo = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.nama