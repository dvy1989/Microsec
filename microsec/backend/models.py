from django.db.models import Model, CharField, ForeignKey, FloatField, DateTimeField, CASCADE


class Sensor(Model):
    name = CharField(max_length=150, primary_key=True)


class Measure(Model):
    sensor = ForeignKey(Sensor, to_field='name', on_delete=CASCADE)
    value = FloatField()
    timestamp = DateTimeField()
