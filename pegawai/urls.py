# pegawai_app/urls.py

from django.urls import path
from .views import pegawai_with_koordinator_view,pegawai_by_unit_kerja, pegawai_create, pegawai_list, pegawai_detail, pegawai_update, pegawai_delete
from .views_pangkat_golongan import index as pg_list, create as pg_create, detail as pg_detail, delete as pg_delete, update as pg_update
from .views_koorsub import index as koorsub_list, create as koorsub_create, detail as koorsub_detail, delete as koorsub_delete, update as koorsub_update


urlpatterns = [
    path('pegawai-with-koordinator/', pegawai_with_koordinator_view, name='pegawai_with_koordinator'),
    path('pegawai-by-unit-kerja/', pegawai_by_unit_kerja, name='pegawai_with_unit_kerja'),
        path('', pegawai_list, name='pegawai_list'),
    path('create/', pegawai_create, name='pegawai_create'),
    path('<int:pk>/', pegawai_detail, name='pegawai_detail'),
    path('<int:pk>/update/', pegawai_update, name='pegawai_update'),
    path('<int:pk>/delete/', pegawai_delete, name='pegawai_delete'),
    path('pangkat_golongan/', pg_list, name='pangkat_golongan_index'),
    path('pangkat_golongan/create/', pg_create, name='pangkat_golongan_create'),
    path('pangkat_golongan/<int:pk>/', pg_detail, name='pangkat_golongan_detail'),
    path('pangkat_golongan/<int:pk>/update/', pg_update, name='pangkat_golongan_update'),
    path('pangkat_golongan/delete/<int:pk>/', pg_delete, name='pangkat_golongan_delete'),

    path('korsub/', koorsub_list, name='koorsub_index'),
    path('korsub/create/', koorsub_create, name='koorsub_create'),
    path('korsub/<int:pk>/', koorsub_detail, name='koorsub_detail'),
    path('korsub/<int:pk>/update/', koorsub_update, name='koorsub_update'),
    path('korsub/delete/<int:pk>/', koorsub_delete, name='koorsub_delete'),
    # Other URL patterns
]
