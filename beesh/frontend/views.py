from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from core.models import Hive, Apiary


class ApiaryListView(LoginRequiredMixin, ListView):
    template_name = 'frontend/apiary_list.html'

    def get_queryset(self):
        return self.request.user.apiaries.all()


class ApiaryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'frontend/apiary_detail.html'
    context_object_name = 'apiary'

    def get_queryset(self):
        return self.request.user.apiaries.all()


class HiveDetailView(LoginRequiredMixin, DetailView):
    template_name = 'frontend/hive_detail.html'
    context_object_name = 'hive'

    def get_queryset(self):
        return Hive.objects.filter(apiary__owner=self.request.user)


class HiveCreateView(LoginRequiredMixin, CreateView):
    template_name = 'frontend/hive_form.html'
    model = Hive
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.apiary = Apiary.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)