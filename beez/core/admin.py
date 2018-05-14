from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class SettingsInline(admin.StackedInline):
    model = models.Settings
    can_delete = False


class QueenInline(admin.StackedInline):
    model = models.Queen


class UserAdmin(BaseUserAdmin):
    inlines = [SettingsInline]


class HiveAdmin(admin.ModelAdmin):
    inlines = [QueenInline]


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)

admin.site.register(models.Apiary)
admin.site.register(models.Hive, HiveAdmin)
admin.site.register(models.Inspection)
admin.site.register(models.Harvest)
admin.site.register(models.File)
