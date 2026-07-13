from django.contrib import admin
from .models import EquipmentCategory, Equipment


@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ['nomi']


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'kategoriya', 'narxi_diapazoni']
    list_filter = ['kategoriya']
    search_fields = ['nomi']
