from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from core.models import Settings


class SettingsView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Settings
    template_name = 'frontend/settings.html'
    fields = ['weight_unit', 'temperature_unit']
    success_url = reverse_lazy('frontend:settings')
    success_message = 'Settings saved'

    def get_object(self, queryset=None):
        return self.request.user.settings

