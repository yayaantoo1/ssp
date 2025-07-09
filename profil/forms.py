from django.forms import ModelForm
from . models import Barang, Hero, About 
from django.core.exceptions import ValidationError
from django import forms

class FormBarang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'
        widgets={
            'kdbrg': forms. TextInput(attrs={'class':'form-control'}),
            'nama' :forms.TextInput(attrs={'class': 'form-control'}),
            'stok' : forms.NumberInput(attrs={'class':'form-control'}),
            'harga': forms.NumberInput(attrs={'class':'form-control'}),
            'link_gbr' : forms. TextInput(attrs={'class':'form-control'}),
            'jenis_id' : forms.Select(attrs={'class':'form-control'}),
        }


#uas
class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and Hero.objects.exists():
            raise ValidationError("Hanya boleh ada satu data Hero.")
        return cleaned_data
    
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and About.objects.exists():
            raise ValidationError("Hanya boleh ada satu data About.")
        return cleaned_data
    
class ContactForm(forms.Form):
    nama = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full bg-slate-200 text-dark p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-primary',
            'placeholder': 'Nama Lengkap Anda'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full bg-slate-200 text-dark p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-primary',
            'placeholder': 'Alamat Email Anda'
        })
    )
    pesan = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full bg-slate-200 text-dark p-3 rounded-md focus:outline-none focus:ring-2 focus:ring-primary h-32',
            'placeholder': 'Tuliskan pesan Anda...'
        })
    )