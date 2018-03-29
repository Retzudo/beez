from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from core.models import Apiary, Hive
from frontend import weather


class ApiaryListView(LoginRequiredMixin, ListView):
    template_name = 'frontend/apiary/list.html'
    context_object_name = 'apiaries'

    def get_queryset(self):
        return self.request.user.apiaries.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_hives'] = Hive.objects.filter(apiary__owner=self.request.user).count()

        return context


class ApiaryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'frontend/apiary/detail.html'
    context_object_name = 'apiary'

    def get_queryset(self):
        return self.request.user.apiaries.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        apiary = context.get('apiary')
        units = {
            'celsius': 'metric',
            'fahrenheit': 'imperial'
        }
        context['weather'] = weather.get_daily_forecast(
            latitude=apiary.latitude,
            longitude=apiary.longitude,
            units=units[self.request.user.settings.temperature],
        )
        context['total_weight'] = sum(hive.last_recorded_weight for hive in apiary.hives.all())

        return context


class ApiaryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'frontend/apiary/form.html'
    model = Apiary
    fields = ['name', 'latitude', 'longitude', 'address', 'radius', 'notes']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ApiaryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'frontend/apiary/form.html'
    model = Apiary
    fields = ['name', 'latitude', 'longitude', 'address', 'radius', 'notes']

    def get_queryset(self):
        return self.request.user.apiaries.all()