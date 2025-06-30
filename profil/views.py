from django.shortcuts import render
from .models import About
from .forms import FormBarang

# Create your views here.
def home(request):
    about = About.objects.first()
    return render(request,'index.html', {'about':about})

def berita(request):
    return render(request,'berita.html')

def form_brg(request):
    form_brg = FormBarang()
    return render(request,'tambah_brg.html', {'form_brg': form_brg})