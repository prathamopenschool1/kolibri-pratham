from rest_framework import serializers

from kolibri.auth.models import Facility

from .models import DataStore


class DataStoreSerializer(serializers.ModelSerializer):
    data = serializers.JSONField(default='\{\}')
    filter_name = serializers.CharField(default='enter filter')
    table_name = serializers.CharField(default='enter name')
    facility = serializers.PrimaryKeyRelatedField(queryset=Facility.objects.all())

    class Meta:
        model = DataStore
        fields = (
            'id', 'data', 'filter_name', 'table_name', 'facility',
        )
