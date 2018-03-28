from rest_framework import viewsets

from api import serializers
from core import models


class ApiaryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ApiarySerializer

    def get_queryset(self):
        return self.request.user.apiaries.all()


class HiveViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HiveSerializer
    filter_fields = ['apiary']

    def get_queryset(self):
        return models.Hive.objects.filter(
            apiary__owner=self.request.user
        )

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        if kwargs.get('many'):
            return serializer
        serializer.fields['apiary'].queryset = models.Apiary.objects.filter(
            owner=self.request.user
        )

        return serializer


class InspectionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.InspectionSerializer
    filter_fields = ['hive']

    def get_queryset(self):
        return models.Inspection.objects.filter(
            hive__apiary__owner=self.request.user
        )

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        if kwargs.get('many'):
            return serializer
        serializer.fields['hive'].queryset = models.Hive.objects.filter(
            apiary__owner=self.request.user
        )

        return serializer


class HarvestViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HarvestSerializer
    filter_fields = ['hive']

    def get_queryset(self):
        return models.Harvest.objects.filter(
            hive__apiary__owner=self.request.user
        )

    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        if kwargs.get('many'):
            return serializer
        serializer.fields['hive'].queryset = models.Hive.objects.filter(
            apiary__owner=self.request.user
        )

        return serializer
