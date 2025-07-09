from django.shortcuts import render

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .models import About, Jenis, Barang, Portofolio, Hero, Client
from .forms import FormBarang, ContactForm 

# Create your views here.
def beranda(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nama = form.cleaned_data['nama']
            email = form.cleaned_data['email']
            pesan = form.cleaned_data['pesan']

            send_mail(
                f'Pesan Baru dari {nama}',
                pesan,
                email, 
                [settings.EMAIL_HOST_USER], 
            )
            
            messages.success(request, 'Pesan Anda telah berhasil terkirim!')

            return redirect('beranda') 
    else:
        form = ContactForm()
    
    hero_data = Hero.objects.first()
    portfolio_items = Portofolio.objects.all()
    client_items = Client.objects.all()
    
    context = {
        'hero': hero_data,
        'portofolio': portfolio_items,
        'clients': client_items,
        'form': form, 
    }

    return render(request, 'index.html', context)

# def tentang(request):
#     about = About.objects.first()
#     return render(request,'about.html', {'about':about})

def pekerjaan(request):
    about = About.objects.first()
    return render(request,'pekerjaan.html', {'about':about})

def kontak(request):
    about = About.objects.first()
    return render(request,'kontak.html', {'about':about})

def berita(request):
    return render(request,'berita.html')

def form_brg(request):
    form_brg = FormBarang()
    return render(request,'tambah_brg.html', {'form_brg': form_brg})

def tentang(request): # Nama view bisa apa saja
    # Ambil satu-satunya data About
    data_about = About.objects.first()
    
    # Kirim data ke template dengan nama 'about'
    context = {
        'about': data_about,
    }

    # Ganti 'nama_template_anda.html' dengan nama file HTML ini
    return render(request, 'about.html', context) 