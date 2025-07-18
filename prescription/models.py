from django.db import models
from patient.models import PatientCase
from doctor.models import Doctor
from medicine.models import Medicine
# Create your models here.


class Prescription(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True , related_name='prescriptions')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE , related_name='prescriptions')
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)  # e.g. "2x/day"
    duration_days = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    prescribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicine.name} for Case #{self.patient_case.id}"