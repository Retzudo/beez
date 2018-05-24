from rest_framework import serializers

from core import models


class ApiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Apiary
        exclude = ['owner']


class QueenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Queen
        fields = ['year', 'number']


class HiveSerializer(serializers.ModelSerializer):
    queen = QueenSerializer(required=False, allow_null=True)

    class Meta:
        model = models.Hive
        fields = '__all__'

    def create(self, validated_data):
        queen_data = validated_data.pop('queen') if 'queen' in validated_data else None

        hive = super().create(validated_data)

        if queen_data:
            models.Queen.objects.create(hive=hive, **queen_data)

        return hive

    def update(self, hive, validated_data):
        queen_data = validated_data.pop('queen') if 'queen' in validated_data else None
        queen = None

        if queen_data is None:
            try:
                hive.queen.delete()
            except models.Queen.DoesNotExist:
                pass
        else:
            try:
                queen = hive.queen
            except models.Queen.DoesNotExist:
                queen = models.Queen(hive=hive)

            queen.year = queen_data['year']
            queen.number = queen_data['number']
            queen.save()

        hive.queen = queen

        return super().update(hive, validated_data)


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inspection
        fields = '__all__'


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Harvest
        fields = '__all__'


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settings
        exclude = ['id', 'user']
