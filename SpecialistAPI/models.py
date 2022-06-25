from django.db import models


class Specialist(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=20)
    worker = models.CharField(max_length=50)
    begining_worked_day = models.TimeField()
    ending_worked_day = models.TimeField()
    appointment = models.IntegerField()
