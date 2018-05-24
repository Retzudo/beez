from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers
from core import models


class ApiaryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ApiarySerializer

    def get_queryset(self):
        return self.request.user.apiaries.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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
        query_set = models.Inspection.objects.filter(
            hive__apiary__owner=self.request.user
        )

        if self.request.query_params.get('hasWeight'):
            query_set = query_set.filter(weight__isnull=False)

        return query_set.order_by('date')

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


class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q')

        apiaries = models.Apiary.search(query)
        hives = models.Hive.search(query)

        return Response({
            'apiaries': serializers.ApiarySerializer(apiaries, many=True).data,
            'hives': serializers.HiveSerializer(hives, many=True).data,
        })


class UpdateSettingsView(RetrieveUpdateAPIView):
    serializer_class = serializers.SettingsSerializer

    def get_object(self):
        return self.request.user.settings