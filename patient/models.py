from django.db import models
from django.contrib.auth.models import User
from hospital.models import Hospital
from doctor.models import Doctor
from symptoms.models import Symptom
from diseases.models import Disease

# Create your models here.

# ===============================
# PATIENT CASES & PRESCRIPTIONS
# ===============================

class PatientCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('unknown', 'Unknown')
    ])
    reported_symptoms = models.ManyToManyField(Symptom, through='patientsymptoms.PatientSymptom')
    suggested_diseases = models.ManyToManyField(Disease, through='diagnosis.AIDiagnosis')
    is_emergency = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patient Case #{self.id}"
