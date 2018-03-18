from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView

from core.models import Hive, Apiary


class HiveDetailView(LoginRequiredMixin, DetailView):
    template_name = 'frontend/hive/detail.html'
    context_object_name = 'hive'

    def get_queryset(self):
        return Hive.objects.filter(apiary__owner=self.request.user)


class HiveCreateView(LoginRequiredMixin, CreateView):
    template_name = 'frontend/hive/form.html'
    model = Hive
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.apiary = Apiary.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class HiveUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'frontend/hive/form.html'
    model = Hive
    fields = ['name', 'description']