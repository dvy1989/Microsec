from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import index, service_worker, get_sensors

router = DefaultRouter()
router.register('sensors', get_sensors)

app_name = 'backend'
urlpatterns = [
    path('', index, name='index'),
    path('service-worker.js', service_worker),
    path('api/', include(router.urls))
]
