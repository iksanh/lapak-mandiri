from django.contrib import admin
from .models import KoordinatorSubstansi

# Register your models here.

class KoordinatorSubstansiAdmin(admin.ModelAdmin):
   list_display = ('nama', 'sub_unit_kerja',)
   search_fields = ('nama', 'sub_unit_kerja',)
   list_filter = ('sub_unit_kerja',)


admin.site.register(KoordinatorSubstansi,KoordinatorSubstansiAdmin)
