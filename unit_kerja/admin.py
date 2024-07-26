from django.contrib import admin
from .models import UnitKerja, SubUnitKerja, UnitKerja_SubUnitKerja

# Register your models here.

admin.site.register(UnitKerja)
admin.site.register(SubUnitKerja)
admin.site.register(UnitKerja_SubUnitKerja)