from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from api import views

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'apiaries', views.ApiaryViewSet, base_name='apiaries')

urlpatterns = [
    path('auth', obtain_jwt_token),
    path('', include(router.urls)),
]