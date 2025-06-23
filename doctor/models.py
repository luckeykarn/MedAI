from django.db import models
from hospital.models import Hospital
from django.contrib.auth.models import User

# Create your models here.
class Speciality(models.Model):
    specialty = models.CharField(max_length=100, blank=True, null=True)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}"

