from django.conf.urls import url
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from api import views

app_name = 'api'

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'apiaries', views.ApiaryViewSet, base_name='apiary')
router.register(r'hives', views.HiveViewSet, base_name='hive')
router.register(r'inspections', views.InspectionViewSet, base_name='inspection')
router.register(r'harvests', views.HarvestViewSet, base_name='harvest')

schema_view = get_schema_view(
   openapi.Info(
      title="Beez API",
      default_version='v1',
      description="Swagger/OpenAPI definition for Beez",
      license=openapi.License(name="GNU GPLv3"),
   ),
   public=True,
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),

    path('auth', obtain_jwt_token),
    path('auth/refresh', refresh_jwt_token),

    path('stats/hives/<int:pk>/weight', views.HiveWeightView.as_view()),

    path('search', views.SearchView.as_view()),

    path('', include(router.urls)),
]