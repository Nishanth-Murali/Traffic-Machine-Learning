from django.db import models

# Create your models here.
class Data(models.Model):
    VEHICLE_CLASS_CHOICES = [('Light', 'Light'), ('Bicycle', 'Bicycle'), ('Bus', 'Bus'), ('ArticulatedTruck', 'ArticulatedTruck'),
     ('SingleUnitTruck', 'SingleUnitTruck')]
    ENTRANCE_CHOICES = [('E', 'East'), ('W', 'West'), ('N', 'North'), ('S', 'South')]
    EXIT_CHOICES = [('E', 'East'), ('W', 'West'), ('N', 'North'), ('S', 'South')]
    timestamp = models.DateTimeField()
    vehicle_class = models.CharField(max_length=20, choices=VEHICLE_CLASS_CHOICES)
    entrance = models.CharField(max_length=1, choices=ENTRANCE_CHOICES)
    exit = models.CharField(max_length=1, choices=EXIT_CHOICES)
    quantity = models.IntegerField(null=True)
