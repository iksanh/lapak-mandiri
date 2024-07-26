from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PangkatGolonganViewSet, PegawaiViewSet, PegawaiKoordinatorSubstansiViewSet, PegawaiSelectViewSet, PegawaiCountByStatusView

router = DefaultRouter()
router.register(r'pangkatgolongan', PangkatGolonganViewSet)
router.register(r'pegawai', PegawaiViewSet)
router.register(r'pegawaiselect', PegawaiSelectViewSet, basename='pegawai-select')
router.register(r'pegawaikoordinatorsubstansi', PegawaiKoordinatorSubstansiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
