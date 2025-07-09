from .models import About

def footer_data(request):
    """
    Menyediakan data dari model About untuk semua template.
    """
    # Ambil satu-satunya objek About dari database
    about_data = About.objects.first()
    
    # Kembalikan data dalam bentuk dictionary.
    # Key 'about' akan menjadi nama variabel di template.
    return {'about': about_data}

# setting di setting.py bagian template