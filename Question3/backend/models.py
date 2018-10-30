from django.db.models import Model, CharField, ForeignKey, FloatField, DateTimeField, CASCADE


class Sensor(Model):
    """
    Sensor
    """
    name = CharField(max_length=150, primary_key=True)


class Measure(Model):
    """
    This model represents a single measurement of the temperature
    If sensor is dropped all associated measurements are dropped as well
    """
    sensor = ForeignKey(Sensor, to_field='name', on_delete=CASCADE)
    value = FloatField()
    timestamp = DateTimeField()
