from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Sensor


class SensorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('name',)
