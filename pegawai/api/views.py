from django.db.models import Count
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from pegawai.models import PangkatGolongan, Pegawai, PegawaiKoordinatorSubstansi
from .serializers import PangkatGolonganSerializer, PegawaiSerializer, PegawaiKoordinatorSubstansiSerializer, PegawaiDetailSerializer, PegawaiSelectSerializer

class PangkatGolonganViewSet(viewsets.ModelViewSet):
    queryset = PangkatGolongan.objects.all()
    serializer_class = PangkatGolonganSerializer

class PegawaiPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 50

class PegawaiViewSet(viewsets.ModelViewSet):
    queryset = Pegawai.objects.all()
    pagination_class = PegawaiPagination


    def get_serializer_class(self):
        if self.action=='list':
            return PegawaiSerializer
        return PegawaiDetailSerializer

class PegawaiSelectViewSet(viewsets.ModelViewSet):
    serializer_class = PegawaiSelectSerializer

    def get_queryset(self):
        queryset=  Pegawai.objects.all()
        unit_kerja = self.request.query_params.get('unit_kerja')
        if unit_kerja:
            queryset = queryset.filter(unit_kerja=unit_kerja).exclude(jabatan__icontains='kepala')

        return queryset

class PegawaiKoordinatorSubstansiViewSet(viewsets.ModelViewSet):
    queryset = PegawaiKoordinatorSubstansi.objects.all()
    serializer_class = PegawaiKoordinatorSubstansiSerializer
    pagination_class = PegawaiPagination
    filter_backends = [OrderingFilter]
    ordering_fields =  ['unit_kerja', 'koordinator_substansi__sub_unit_kerja']

class PegawaiCountByStatusView(APIView):
    def get(self, request, format=None):
        total_pegawai = Pegawai.objects.count()
        counts = Pegawai.objects.values('status').annotate(total=Count('status'))

        for item in counts:
            percentage = (item['total'] / total_pegawai) * 100
            item['percentage'] = f"{percentage:.2f}"
        return Response(counts, status=status.HTTP_200_OK)
