from rest_framework import serializers
from .models import DataModel
from datastore.serializer import DetailDatasetSerializer

class DataModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataModel
        fields = ['name', 'user']


class DetailDataModelSerializer(serializers.ModelSerializer):
    dataset=DetailDatasetSerializer()
    class Meta:
        model = DataModel
        fields = '__all__'

