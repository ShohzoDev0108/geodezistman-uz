from django.contrib import admin
from .models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'til', 'turi', 'yuklangan_sana']
    list_filter = ['til', 'turi']
    search_fields = ['nomi']
