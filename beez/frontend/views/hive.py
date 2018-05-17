from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from private_storage.views import PrivateStorageDetailView

from core.models import Hive, Apiary, File, Queen


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


class HiveDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'frontend/hive/delete.html'
    model = Hive

    def get_queryset(self):
        return Hive.objects.filter(apiary__owner=self.request.user)

    def get_success_url(self):
        return self.get_object().apiary.get_absolute_url()


class HiveFileView(LoginRequiredMixin, CreateView):
    template_name = 'frontend/hive/file_form.html'
    model = File
    fields = ['file']

    def get_success_url(self):
        return reverse('frontend:hive-detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        form.instance.hive = get_object_or_404(Hive, pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class HiveFileDownloadView(LoginRequiredMixin, PrivateStorageDetailView):
    model = File
    model_file_field = 'file'
    content_disposition = True

    def get_queryset(self):
        return super().get_queryset().filter(hive__isnull=False, hive__owner=self.request.user)


class HiveFileDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'frontend/hive/file_delete.html'
    model = File
    context_object_name = 'file'

    def get_queryset(self):
        return File.objects.filter(hive__apiary__owner=self.request.user)

    def get_success_url(self):
        return self.object.hive.get_absolute_url()


class QueenEditView(LoginRequiredMixin, UpdateView):
    template_name = 'frontend/hive/queen/form.html'
    model = Queen
    fields = ['year', 'number']

    def get_queryset(self):
        return Queen.objects.filter(hive__apiary__owner=self.request.user)

    def get_object(self, queryset=None):
        qs = self.get_queryset() if queryset is None else queryset
        return qs.get(hive__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hive'] = self.get_object().hive

        return context


class QueenCreateView(LoginRequiredMixin, CreateView):
    template_name = 'frontend/hive/queen/form.html'
    model = Queen
    fields = ['year', 'number']

    def get_success_url(self):
        return reverse('frontend:hive-detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        form.instance.hive = get_object_or_404(Hive, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hive'] = get_object_or_404(Hive, pk=self.kwargs.get('pk'))

        return context


class QueenDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'frontend/hive/queen/delete.html'
    model = Queen
    context_object_name = 'queen'

    def get_queryset(self):
        return Queen.objects.filter(hive__apiary__owner=self.request.user)

    def get_object(self, queryset=None):
        qs = self.get_queryset() if queryset is None else queryset
        return qs.get(hive__pk=self.kwargs['pk'])

    def get_success_url(self):
        return self.object.hive.get_absolute_url()
