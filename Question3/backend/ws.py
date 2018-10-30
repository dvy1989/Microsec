from datetime import datetime
from json import dumps
from random import randint
from threading import Thread
from time import sleep

from pytz import UTC
from websocket import create_connection

from .models import Sensor, Measure


class WebSocketServer(object):
    """
    This is an adapter for socket server
    It uses implementation of web socket client for Python
    to collaborate with broker
    """
    def __init__(self):
        self.connection = create_connection('ws://localhost:5000')

    def start(self):
        Thread(target=self.feed).start()

    def feed(self):
        while True:
            try:
                sensors = Sensor.objects.all()
                for sensor in sensors:
                    timestamp = datetime.utcnow()
                    timestamp = datetime(timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second, timestamp.microsecond, UTC)
                    value = randint(0, 50) - 15
                    measure = Measure(value=value, timestamp=timestamp, sensor=sensor)
                    measure.save()
                    self.send(dumps({'type': 'VALUE', 'value': value, 'name': sensor.name}))
                sleep(5)
            except:
                pass

    def send(self, message):
        self.connection.send(message)


WEB_SOCKET = WebSocketServer()
WEB_SOCKET.start()
