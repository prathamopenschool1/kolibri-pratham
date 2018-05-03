from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from pip._vendor.html5lib import filters
from rest_framework import viewsets

from kolibri.auth.api import KolibriAuthPermissionsFilter

from .models import DataStore
from .serializers import DataStoreSerializer
from django.http import HttpResponse


class DataStoreViewset(viewsets.ModelViewSet):
    model = DataStore
    serializer_class = DataStoreSerializer
    filter_backends = (KolibriAuthPermissionsFilter, DjangoFilterBackend, SearchFilter,)
    queryset = DataStore.objects.all()#raw('SELECT * FROM DataStore where filter_name = %s', [filter_name])
    filter_fields = ('filter_name', 'table_name')
    #search_fields = ('^filter_name', '^table_name')
    #result = DataStore.objects.filter(filter_fields__icontains='filter_name')

    '''
    def get_queryset(self):
        queryset = DataStore.objects.all()
        filter_name = self.request.query_params.get('filter_name', None)
        table_name = self.request.query_params.get('table_name', None)

        if filter_name:
            queryset = queryset.filter(filter_name__icontains=filter_name)
        if table_name:
            queryset = queryset.filter(table_name=table_name)
        elif filter_name and table_name:
            queryset = queryset.filter(filter_name__icontains=filter_name, table_name=table_name)

        return queryset'''
