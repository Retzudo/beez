from django.views.generic import UpdateView

from core.models import Settings


class SettingsView(UpdateView):
    model = Settings
    template_name = 'frontend/settings.html'

    def get_object(self, queryset=None):
        return self.request.user.settings

