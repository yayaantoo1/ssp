from django.contrib import admin
from .forms import HeroForm, AboutForm

# Register your models here.
from .models import Barang,Jenis,About , Portofolio, Hero, Client


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

# Register your models here.


class BarangAdmin(admin.ModelAdmin):
    list_display = ('kdbrg','nama','stok','harga','link_gmb','jenis_id')
    list_filter = ('jenis_id',)
    search_fields = ('nama','harga','jenis_id__nama')
    list_per_page = 4


#uas
class PortofolioAdmin(ModelAdmin):
    list_display = ['judul', 'deskripsi']
    search_fields = ['judul', 'deskripsi']

class HeroAdmin(ModelAdmin):
    list_display = ('nama', 'profesi')
    
    # Mencegah ada lebih dari satu data Hero
    def has_add_permission(self, request):
        return not Hero.objects.exists()


    def has_add_permission(self, request):
        return not Hero.objects.exists()

    #klien
class ClientAdmin(ModelAdmin):
    list_display = ('nama',)

class AboutAdmin(ModelAdmin):
    form = AboutForm
    list_display = ['judul']
    search_fields = ['judul', 'deskripsi']

    def has_add_permission(self, request):
        return not About.objects.exists()





# admin.site.register(Barang, BarangAdmin)

# admin.site.register(Jenis)

admin.site.register(About, AboutAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(Portofolio, PortofolioAdmin)
admin.site.register(Client, ClientAdmin)