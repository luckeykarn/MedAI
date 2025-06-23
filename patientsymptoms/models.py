from django.db import models

# Create your models here.

class PatientSymptom(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    severity = models.CharField(max_length=20, choices=[
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ])
    duration_days = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together = [['patient_case', 'symptom']]