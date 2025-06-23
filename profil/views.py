from django.shortcuts import render
from .models import About

# Create your views here.
def home(request):
    about = About.objects.first()
    return render(request,'index.html', {'about':about})

def berita(request):
    return render(request,'berita.html')