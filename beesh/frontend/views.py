from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView


class ApiaryListView(LoginRequiredMixin, ListView):
    template_name = 'frontend/apiary_list.html'

    def get_queryset(self):
        return self.request.user.apiaries.all()


class ApiaryDetailView(LoginRequiredMixin, DetailView):
    template_name = 'frontend/apiary_detail.html'
    context_object_name = 'apiary'

    def get_queryset(self):
        return self.request.user.apiaries.all()