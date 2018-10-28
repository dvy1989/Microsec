from os.path import join

from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED


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


@api_view(['GET'])
def get_sensors(request):
    if request.user.is_authentificated:
        return Response(status=HTTP_200_OK)
    else:
        return Response(status=HTTP_401_UNAUTHORIZED)
