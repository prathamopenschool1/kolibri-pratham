from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from kolibri.auth.api import KolibriAuthPermissionsFilter

from .models import DataStore
from .serializers import DataStoreSerializer

class DataStoreViewset(viewsets.ModelViewSet):
    serializer_class = DataStoreSerializer
    filter_backends = (KolibriAuthPermissionsFilter, DjangoFilterBackend)
    queryset = DataStore.objects.all()
