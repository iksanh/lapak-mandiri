from django.urls import path
from .views import index, create, update,delete
from .views_persayaratan import index as index_persayaratan, create as create_persyaratan, update as update_persyaratan, delete as delete_persyaratan
from .views_pengajuan import index as index_pengajuan, create as create_pengajuan, update as update_pengajuan, delete as delete_pengajuan


urlpatterns = [
    path('', index, name='layanan_list'),
    path('create/', create, name='layanan_create'),
    path('update/<int:pk>/', update, name='layanan_update'),
    path('delete/<int:pk>/', delete, name='layanan_delete'),
    path('persyaratan/', index_persayaratan, name='persyaratan_list'),
    path('persyaratan/create/', create_persyaratan, name='persyaratan_create'),
    path('persyaratan/update/<int:pk>/', update_persyaratan, name='persyaratan_update'),
    path('persyaratan/delete/<int:pk>/', delete_persyaratan, name='persyaratan_delete'),


    path('pengajuan/', index_pengajuan, name='pengajuan_list'),
    path('pengajuan/create/<str:encrypted_id>/', create_pengajuan, name='pengajuan_create'),
    path('pengajuan/update/<int:pk>/', update_pengajuan, name='pengajuan_update'),
    path('pengajuan/delete/<int:pk>/', delete_pengajuan, name='pengajuan_delete'),
    # Add URLs for PersyaratanLayanan and PengajuanLayanan similarly.
]