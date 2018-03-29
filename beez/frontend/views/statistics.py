from django.views.generic import TemplateView

from core.models import Apiary, Hive, Inspection


class StatisticsView(TemplateView):
    template_name = 'frontend/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        apiaries = Apiary.objects.filter(owner=self.request.user)
        hives = Hive.objects.filter(apiary__owner=self.request.user)
        context['total_apiaries'] = apiaries.count()
        context['total_hives'] = hives.count()
        context['total_weight'] = sum(hive.last_recorded_weight for hive in hives)

        return context
