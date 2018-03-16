from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

from frontend import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='frontend/index.html'), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.RegisterView.as_view(), name='register'),
    path('dashboard/apiaries', views.ApiaryListView.as_view(), name='apiary-list'),
    path('dashboard/apiaries/create-apiary', views.ApiaryCreateView.as_view(), name='apiary-create'),
    path('dashboard/apiaries/<int:pk>', views.ApiaryDetailView.as_view(), name='apiary-detail'),
    path('dashboard/apiaries/<int:pk>/edit', views.ApiaryUpdateView.as_view(), name='apiary-edit'),
    path('dashboard/apiaries/<int:pk>/create-hive', views.HiveCreateView.as_view(), name='hive-create'),
    path('dashboard/hives/<int:pk>', views.HiveDetailView.as_view(), name='hive-detail'),
]