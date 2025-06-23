from django.db import models
from hospital.models import Hospital
from django.contrib.auth.models import User

# Create your models here.
class Speciality(models.Model):
    specialty = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.specialty


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor")
    speciality = models.ForeignKey(Speciality,on_delete=models.SET_NULL,null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True,related_name="doctors")
    description = models.TextField()

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}"

