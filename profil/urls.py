from django.urls import path
from . import views

urlpatterns = [
    path('', views.beranda ),
    path('tentang', views.tentang ),
    path('pekerjaan', views.pekerjaan ),
    path('kontak', views.kontak ),
    path('berita/', views.berita),
    path('tbh_brg/', views.form_brg),
]