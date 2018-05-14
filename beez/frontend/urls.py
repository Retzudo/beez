from django.urls import path, include
from django.views.generic import TemplateView

from frontend.views import apiary, hive, user, inspection, statistics, settings, search

app_name = 'frontend'

urlpatterns = [
    path('', TemplateView.as_view(template_name='frontend/index.html'), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', user.RegisterView.as_view(), name='register'),
    path('search', search.search, name='search'),

    path('dashboard/apiaries', apiary.ApiaryListView.as_view(), name='apiary-list'),
    path('dashboard/apiaries/create-apiary', apiary.ApiaryCreateView.as_view(), name='apiary-create'),
    path('dashboard/apiaries/<int:pk>', apiary.ApiaryDetailView.as_view(), name='apiary-detail'),
    path('dashboard/apiaries/<int:pk>/edit', apiary.ApiaryUpdateView.as_view(), name='apiary-edit'),
    path('dashboard/apiaries/<int:pk>/add-file', apiary.ApiaryFileView.as_view(), name='apiary-add-file'),
    path('dashboard/apiaries/<int:pk>/create-hive', hive.HiveCreateView.as_view(), name='hive-create'),
    path('dashboard/apiaries/files/<int:pk>', apiary.ApiaryFileDownloadView.as_view(), name='apiary-file'),
    path('dashboard/apiaries/files/<int:pk>/delete', apiary.ApiaryFileDeleteView.as_view(), name='apiary-file-delete'),

    path('dashboard/hives/<int:pk>', hive.HiveDetailView.as_view(), name='hive-detail'),
    path('dashboard/hives/<int:pk>/edit', hive.HiveUpdateView.as_view(), name='hive-edit'),
    path('dashboard/hives/<int:pk>/add-file', hive.HiveFileView.as_view(), name='hive-add-file'),
    path('dashboard/hives/<int:pk>/transfer', hive.HiveTransferView.as_view(), name='hive-transfer'),
    path('dashboard/hives/<int:pk>/terminate', hive.HiveTerminateView.as_view(), name='hive-terminate'),
    path('dashboard/hives/<int:pk>/delete', lambda x: None, name='hive-delete'),
    path('dashboard/hives/<int:pk>/create-inspection', inspection.InspectionCreateView.as_view(), name='inspection-create'),
    path('dashboard/hives/files/<int:pk>', hive.HiveFileDownloadView.as_view(), name='hive-file'),
    path('dashboard/hives/files/<int:pk>/delete', hive.HiveFileDeleteView.as_view(), name='hive-file-delete'),
    path('dashboard/hives/<int:pk>/edit-queen', hive.QueenEditView.as_view(), name='hive-edit-queen'),
    path('dashboard/hives/<int:pk>/add-queen', hive.QueenCreateView.as_view(), name='hive-add-queen'),
    path('dashboard/hives/<int:pk>/delete-queen', hive.QueenDeleteView.as_view(), name='hive-delete-queen'),

    path('dashboard/inspections/<int:pk>', inspection.InspectionDetailView.as_view(), name='inspection-detail'),
    path('dashboard/inspections/<int:pk>/edit', inspection.InspectionUpdateView.as_view(), name='inspection-edit'),
    path('dashboard/inspections/<int:pk>/delete', inspection.InspectionDeleteView.as_view(), name='inspection-delete'),

    path('dashboard/statistics', statistics.StatisticsView.as_view(), name='statistics'),
    path('dashboard/settings', settings.SettingsView.as_view(), name='settings'),
]
