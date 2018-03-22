from rest_framework import serializers

from core import models


class ApiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Apiary
        exclude = ['owner']


class HiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hive
        fields = '__all__'


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inspection
        fields = '__all__'


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Harvest
        fields = '__all__'
