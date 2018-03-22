from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'api'

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('auth', obtain_jwt_token),
]