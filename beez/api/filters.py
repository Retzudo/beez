from django_filters import rest_framework as filters

from core import models


class InspectionFilter(filters.FilterSet):
    has_weight = filters.BooleanFilter(field_name='weight', lookup_expr='isnull', exclude=True)
    has_mites = filters.BooleanFilter(field_name='mites_counted', lookup_expr='isnull', exclude=True)

    class Meta:
        model = models.Inspection
        fields = ['hive']