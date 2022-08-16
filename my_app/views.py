from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import MyApp
from .serializers import AppSerializer
from .permissions import OwnerOnly


class AppListCreateView(ListCreateAPIView):
    queryset = MyApp.objects.all()
    serializer_class = AppSerializer


class AppDetailView(RetrieveUpdateDestroyAPIView):
    queryset = MyApp.objects.all()
    serializer_class = AppSerializer
    permission_classes = [OwnerOnly]

