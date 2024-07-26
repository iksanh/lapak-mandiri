from rest_framework import viewsets
from .serializers import KoordinatorSubstansiSerializer
from koordinator_substansi.models import KoordinatorSubstansi

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, generics, permissions



class KoorsubList(generics.ListCreateAPIView):
    queryset = KoordinatorSubstansi.objects.all()
    serializer_class = KoordinatorSubstansiSerializer
    permission_classes = [permissions.AllowAny]

class KoorsubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KoordinatorSubstansi.objects.all()
    serializer_class = KoordinatorSubstansiSerializer