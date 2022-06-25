from django.db import models
from SpecialistAPI.models import Specialist


class User(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete = models.CASCADE)
    full_name = models.CharField(max_length=70)
    start_reception = models.TimeField()
    finish_reception = models.TimeField()
    date = models.DateField()