# pegawai_app/urls.py

from django.urls import path
from .views import pegawai_with_koordinator_view,pegawai_by_unit_kerja

urlpatterns = [
    path('pegawai-with-koordinator/', pegawai_with_koordinator_view, name='pegawai_with_koordinator'),
    path('pegawai-by-unit-kerja/', pegawai_by_unit_kerja, name='pegawai_with_unit_kerja'),
    # Other URL patterns
]
