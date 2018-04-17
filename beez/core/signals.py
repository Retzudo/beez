import os

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from core import models
from core.models import Settings


@receiver(post_save, sender=get_user_model())
def user_saved(sender, instance, created, **kwargs):
    if created:
        Settings.objects.create(user=instance)


@receiver(post_delete, sender=models.File)
def delete_file(sender, instance, *args, **kwargs):
    if instance.file:
        path = instance.file.path
        if os.path.isfile(path):
            os.remove(path)