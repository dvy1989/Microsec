from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from websocket import create_connection

from .views import index, service_worker, add_sensor, get_sensors

# router = DefaultRouter()
# router.register('sensors', SensorViewSet)
# router.register('sensor/add', add_sensor)

app_name = 'backend'
urlpatterns = [
    path('', index, name='index'),
    path('service-worker.js', service_worker),
    path('login', obtain_auth_token, name='rest_login'),
    # path('api/', include(router.urls)),
    path('api/sensor/add', add_sensor, name='add_sensor'),
    path('api/sensors/', get_sensors, name='get_sensors'),
]
