from rest_framework import serializers

from kolibri.auth.models import Facility

from .models import DataStore

class DataStoreSerializer(serializers.ModelSerializer):

    data = serializers.JSONField(default='\{\}')
    facility = serializers.PrimaryKeyRelatedField(queryset=Facility.objects.all())

    class Meta:
        model = DataStore
        fields = (
            'id', 'data', 'facility',
        )
