from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView

from core.models import Hive, Apiary
from frontend import weather


class ApiaryListView(LoginRequiredMixin, ListView):
    template_name = 'frontend/apiary_list.html'

    def get_queryset(self):
        return self.request.user.apiaries.all()


class ApiaryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'frontend/apiary_detail.html'
    context_object_name = 'apiary'

    def get_queryset(self):
        return self.request.user.apiaries.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        apiary = context.get('apiary')
        context['weather'] = weather.get_daily_forecast(
            latitude=apiary.latitude,
            longitude=apiary.longitude,
        )

        return context


class ApiaryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'frontend/apiary_form.html'
    model = Apiary
    fields = ['name', 'latitude', 'longitude', 'address', 'radius', 'notes']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ApiaryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'frontend/apiary_form.html'
    model = Apiary
    fields = ['name', 'latitude', 'longitude', 'address', 'radius', 'notes']


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


class HiveUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'frontend/hive_form.html'
    model = Hive
    fields = ['name', 'description']


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'