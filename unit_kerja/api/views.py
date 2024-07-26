from rest_framework import viewsets
from unit_kerja.models import UnitKerja, SubUnitKerja, UnitKerja_SubUnitKerja
from .serializers import UnitKerjaSerializer, SubUnitKerjaSerializer, UnitKerja_SubUnitKerjaSerializer

class UnitKerjaViewSet(viewsets.ModelViewSet):
    queryset = UnitKerja.objects.all()
    serializer_class = UnitKerjaSerializer

class SubUnitKerjaViewSet(viewsets.ModelViewSet):
    queryset = SubUnitKerja.objects.all()
    serializer_class = SubUnitKerjaSerializer

class UnitKerja_SubUnitKerjaViewSet(viewsets.ModelViewSet):
    queryset = UnitKerja_SubUnitKerja.objects.all()
    serializer_class = UnitKerja_SubUnitKerjaSerializer