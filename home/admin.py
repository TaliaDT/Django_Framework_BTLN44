from django.contrib import admin
from .models import SanPham

# Register your models here.
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ['tieude', 'gia', 'ngaythem',]
    search_fields = ['id']
admin.site.register(SanPham, SanPhamAdmin)