from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from core.models import Inspection, Hive


class InspectionDetailView(LoginRequiredMixin, DetailView):
    template_name = 'frontend/inspection/detail.html'
    model = Inspection
    context_object_name = 'inspection'

    def get_queryset(self):
        return Inspection.objects.filter(hive__apiary__owner=self.request.user)


class InspectionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'frontend/inspection/form.html'
    model = Inspection
    fields = ['date', 'weight', 'saw_queen', 'saw_eggs', 'needs_food', 'gave_food', 'how_much_food', 'mites_counted', 'mite_treatment', 'notes']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hive'] = get_object_or_404(Hive, pk=self.kwargs.get('pk'))

        return context

    def form_valid(self, form):
        form.instance.hive = Hive.objects.get(apiary__owner=self.request.user, pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class InspectionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'frontend/inspection/form.html'
    model = Inspection
    fields = ['date', 'weight', 'saw_queen', 'saw_eggs', 'needs_food', 'gave_food', 'how_much_food', 'mites_counted', 'mite_treatment', 'notes']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hive'] = self.get_object().hive

        return context

    def get_queryset(self):
        return Inspection.objects.filter(hive__apiary__owner=self.request.user)


class InspectionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'frontend/inspection/delete.html'
    model = Inspection
    context_object_name = 'inspection'

    def get_queryset(self):
        return Inspection.objects.filter(hive__apiary__owner=self.request.user)

    def get_success_url(self):
        return self.object.hive.get_absolute_url()
