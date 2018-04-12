from django.contrib.auth.mixins import LoginRequiredMixin
from private_storage.views import PrivateStorageDetailView

from core.models import File


class ApiaryFileDownloadView(LoginRequiredMixin, PrivateStorageDetailView):
    model = File
    model_file_field = 'file'

    def get_queryset(self):
        return super().get_queryset().filter(apiary__isnull=False, apiary__owner=self.request.user)


class HiveFileDownloadView(LoginRequiredMixin, PrivateStorageDetailView):
    model = File
    model_file_field = 'file'

    def get_queryset(self):
        return super().get_queryset().filter(hive__isnull=False, hive__owner=self.request.user)
