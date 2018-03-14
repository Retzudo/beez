from django.urls import path
from django.views.generic import TemplateView

from frontend import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='frontend/index.html'), name='index'),
    path('apiaries', views.ApiaryListView.as_view(), name='apiary-list'),
    path('apiaries/<int:pk>', views.ApiaryDetailView.as_view(), name='apiary-detail'),
]