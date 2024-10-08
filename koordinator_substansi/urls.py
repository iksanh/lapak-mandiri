from django.urls import path
from .views import index, create, update, destroy


urlpatterns = [
    path('', index, name='koordinator_substansi_index'),
    path('create/', create, name='koordinator_substansi_create'),
    path('edit/<int:id>', update, name='koordinator_substansi_update'),
    path('delete/<int:id>', destroy, name='koordinator_substansi_delete'),

]