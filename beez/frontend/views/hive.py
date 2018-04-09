from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from core.models import Hive, Apiary


class HiveDetailView(LoginRequiredMixin, DetailView):
    template_name = 'frontend/hive/detail.html'
    context_object_name = 'hive'

    def get_queryset(self):
        return Hive.objects.filter(apiary__owner=self.request.user)


class HiveCreateView(LoginRequiredMixin, CreateView):
    template_name = 'frontend/hive/form.html'
    model = Hive
    fields = ['name', 'description', 'notes', 'makes_honey']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apiary'] = get_object_or_404(Apiary, pk=self.kwargs.get('pk'))

        return context

    def form_valid(self, form):
        form.instance.apiary = Apiary.objects.get(owner=self.request.user, pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class HiveUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'frontend/hive/form.html'
    model = Hive
    fields = ['name', 'description', 'notes', 'makes_honey']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apiary'] = self.get_object().apiary

        return context

    def get_queryset(self):
        return Hive.objects.filter(apiary__owner=self.request.user)


class HiveTransferView(LoginRequiredMixin, UpdateView):
    template_name = 'frontend/hive/transfer.html'
    model = Hive
    fields = ['apiary']

    def _get_available_apiaries(self):
        current_apiary = self.get_object().apiary
        current_user = self.request.user

        return Apiary.objects.filter(owner=current_user).exclude(pk=current_apiary.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_transfer'] = self._get_available_apiaries().count() > 0

        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['apiary'].queryset = self._get_available_apiaries()

        return form


class HiveTerminateView(LoginRequiredMixin, DeleteView):
    template_name = 'frontend/hive/terminate.html'
    model = Hive

    def get_success_url(self):
        return self.get_object().apiary.get_absolute_url()

    def delete(self, request, *args, **kwargs):
        hive = self.get_object()
        hive.terminated = True
        hive.save()

        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)
