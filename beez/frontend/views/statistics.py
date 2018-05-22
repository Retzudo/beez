from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView

from core.models import Apiary, Hive


class StatisticsView(LoginRequiredMixin, TemplateView):
    template_name = 'frontend/statistics/overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        apiaries = Apiary.objects.filter(owner=self.request.user)
        hives = Hive.objects.filter(apiary__owner=self.request.user)
        context['total_apiaries'] = apiaries.count()
        context['total_hives'] = hives.count()
        context['total_weight'] = sum(hive.last_recorded_weight or 0 for hive in hives)

        return context


class HiveStatisticsView(LoginRequiredMixin, DetailView):
    template_name = 'frontend/statistics/hive.html'
    context_object_name = 'hive'

    def get_queryset(self):
        return Hive.objects.filter(apiary__owner=self.request.user)



