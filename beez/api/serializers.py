from rest_framework import serializers

from core import models


class ApiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Apiary
        exclude = ['owner']
