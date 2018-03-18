from django.urls import path, include
from django.views.generic import TemplateView

from frontend.views import apiary, hive, user

urlpatterns = [
    path('', TemplateView.as_view(template_name='frontend/index.html'), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', user.RegisterView.as_view(), name='register'),

    path('dashboard/apiaries', apiary.ApiaryListView.as_view(), name='apiary-list'),
    path('dashboard/apiaries/create-apiary', apiary.ApiaryCreateView.as_view(), name='apiary-create'),
    path('dashboard/apiaries/<int:pk>', apiary.ApiaryDetailView.as_view(), name='apiary-detail'),
    path('dashboard/apiaries/<int:pk>/edit', apiary.ApiaryUpdateView.as_view(), name='apiary-edit'),
    path('dashboard/apiaries/<int:pk>/create-hive', hive.HiveCreateView.as_view(), name='hive-create'),

    path('dashboard/hives/<int:pk>', hive.HiveDetailView.as_view(), name='hive-detail'),
    path('dashboard/hives/<int:pk>/edit', hive.HiveUpdateView.as_view(), name='hive-edit'),
    path('dashboard/hives/<int:pk>/transfer', hive.HiveTransferView.as_view(), name='hive-transfer'),
    path('dashboard/hives/<int:pk>/terminate', lambda x: None, name='hive-terminate'),
    path('dashboard/hives/<int:pk>/delete', lambda x: None, name='hive-delete'),
    path('dashboard/hives/<int:pk>/create-inspection', lambda x: None, name='inspection-create'),

    path('dashboard/inspections/<int:pk>', lambda x: None, name='inspection-details'),
    path('dashboard/inspections/<int:pk>/edit', lambda x: None, name='inspection-edit'),
]
