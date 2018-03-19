from django.contrib import admin

from core import models


admin.site.register(models.Apiary)
admin.site.register(models.Hive)
admin.site.register(models.Inspection)
admin.site.register(models.Harvest)
