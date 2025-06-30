from django.urls import path
from . import views

urlpatterns = [
    path('omah/', views.home ),
    path('berita/', views.berita),
    path('tbh_brg/', views.form_brg),
]