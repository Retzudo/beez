from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, View

from core.models import Hive, Apiary
from frontend import forms


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


class HiveTransferView(LoginRequiredMixin, View):
    template_name = 'frontend/hive/transfer.html'

    def _render(self, form):
        return render(self.request, self.template_name, {
            'form': form
        })

    def get(self, request, pk):
        try:
            hive = Hive.objects.filter(apiary__owner=request.user).get(pk=pk)
        except Hive.DoesNotExist as e:
            raise Http404 from e

        form = forms.TransferHiveForm(user=request.user, current_apiary_pk=hive.apiary.pk)

        return self._render(form)

    def post(self, request, pk):
        try:
            hive = Hive.objects.filter(apiary__owner=request.user).get(pk=pk)
        except Hive.DoesNotExist as e:
            raise Http404 from e

        form = forms.TransferHiveForm(user=request.user, current_apiary_pk=hive.apiary.pk, data=request.POST)

        if form.is_valid():
            hive.apiary = form.cleaned_data['to_apiary']
            return redirect(hive.get_absolute_url())
        else:
            return self._render(form)
