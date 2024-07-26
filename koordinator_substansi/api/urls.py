from django.urls import path, include

from .views import KoorsubList, KoorsubDetail



urlpatterns = [
    path('', KoorsubList.as_view()),
    path('<int:pk>', KoorsubDetail.as_view())
]