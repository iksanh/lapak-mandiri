"""
URL configuration for mapeg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include, reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
#for rest_framework
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from auth.api.views import CustomTokenObtainPairView

from pegawai.api.views import PegawaiCountByStatusView

# def home(request):
#     if request.user.is_authenticated:
#         return  HttpResponseRedirect(reverse('admin:index'))
#     else: 
#         return HttpResponseRedirect(reverse('admin:login'))

@login_required
def index(request):
  return render(request, 'index.html')

urlpatterns = [
    #  path('', home, name='home'),
     path('', index, name='index'),
     path('admin/', admin.site.urls),
     path('auth/', include('auth.urls')),
     path('api/', include('unit_kerja.api.urls')),
     path('api/koordinator_substansi/', include('koordinator_substansi.api.urls')),
     
     path('api/', include('pegawai.api.urls')),
     path('pegawai/', include('pegawai.urls')),
     path('unit_kerja/', include('unit_kerja.urls')),
     path('koorsub/', include('koordinator_substansi.urls')),
     path('layanan/', include('layanan.urls')),
     path('api/rekap/pegawai/',PegawaiCountByStatusView.as_view(), name = 'rekap_pegawai' ),
     path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
