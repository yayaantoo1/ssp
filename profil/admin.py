from django.contrib import admin

# Register your models here.
from .models import Barang,Jenis


class BarangAdmin(admin.ModelAdmin):
    list_display = ('kdbrg','nama','stok','harga','link_gmb','jenis_id')
    list_filter = ('jenis_id',)
    search_fields = ('nama','harga','jenis_id__nama')
    list_per_page = 4


admin.site.register(Barang, BarangAdmin)

admin.site.register(Jenis)