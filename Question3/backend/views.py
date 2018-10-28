from json import dumps
from os.path import join

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Sensor, Measure
from .serializers import SensorSerializer
from .ws import WEB_SOCKET


def load_file(filename):
    try:
        with open(join(settings.REACT_APP, 'build', filename)) as file:
            return HttpResponse(file.read())
    except:
        return HttpResponse('%s not found' % filename, status=404)


def index(request):
    return load_file('index.html')


def service_worker(request):
    return load_file('service-worker.js')


@api_view(['POST'])
def add_sensor(request):
    new_sensor = Sensor(name=request.data["name"])
    new_sensor.save()
    WEB_SOCKET.send(dumps({'type': 'SENSOR', 'name': new_sensor.name}))
    return Response()


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


@api_view(['GET'])
def get_sensors(request):
    json_data = []
    sensors = Sensor.objects.all()
    for sensor in sensors:
        latest_measures = Measure.objects.filter(sensor=sensor).order_by('-timestamp')[:1]
        if len(latest_measures) > 0:
            value = latest_measures[0].value
        else:
            value = None
        json_data.append({'name': sensor.name, 'value': value})
    return JsonResponse(json_data, safe=False)
