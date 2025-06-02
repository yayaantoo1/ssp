from django.contrib import admin

# Register your models here.
from .models import Barang


class BarangAdmin(admin.ModelAdmin):
    list_display = ('kdbrg','nama','stok','harga','link_gmb')
    list_filter = ('nama',)
    search_fields = ('nama','harga')


admin.site.register(Barang, BarangAdmin)

