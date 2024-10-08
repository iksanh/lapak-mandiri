from django.urls import path
from .views import index, create, update, destroy
from .views_sub_unit import index as index_sub, create as create_sub, update as update_sub, destroy as destroy_sub


urlpatterns = [
    path('', index, name='unit_kerja_index'),
    path('create/', create, name='unit_kerja_create'),
    path('edit/<int:id>', update, name='unit_kerja_update'),
    path('delete/<int:id>', destroy, name='unit_kerja_delete'),

    path('sub_unit/', index_sub, name='sub_unit_kerja_index'),
    path('sub_unit/create/', create_sub, name='sub_unit_kerja_create'),
    path('sub_unit/edit/<int:id>', update_sub, name='sub_unit_kerja_update'),
    path('sub_unit/delete/<int:id>', destroy_sub, name='sub_unit_kerja_delete'),

    # Other URL patterns
]
