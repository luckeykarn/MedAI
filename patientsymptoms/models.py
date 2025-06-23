from django.db import models
from patient.models import PatientCase
from symptoms.models import Symptom
# Create your models here.

class PatientSymptom(models.Model):
    patient = models.ForeignKey(PatientCase, on_delete=models.CASCADE,)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    severity = models.CharField(max_length=20, choices=[
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ])
    duration_days = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together = [['patient', 'symptom']]