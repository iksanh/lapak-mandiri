from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnitKerjaViewSet, SubUnitKerjaViewSet, UnitKerja_SubUnitKerjaViewSet

router = DefaultRouter()
router.register(r'unitkerja', UnitKerjaViewSet)
router.register(r'sub_unit_kerja', SubUnitKerjaViewSet)
router.register(r'unitkerja_subunitkerja', UnitKerja_SubUnitKerjaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
