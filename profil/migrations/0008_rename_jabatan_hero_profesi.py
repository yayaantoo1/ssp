# Generated by Django 5.2.1 on 2025-07-08 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0007_rename_judul_hero_nama_rename_deskripsi_hero_tagline_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='jabatan',
            new_name='profesi',
        ),
    ]
