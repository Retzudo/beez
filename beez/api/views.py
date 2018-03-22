from rest_framework import viewsets

from api import serializers


class ApiaryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ApiarySerializer

    def get_queryset(self):
        return self.request.user.apiaries.all()
