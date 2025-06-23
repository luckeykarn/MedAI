from django.db import models
from patient.models import PatientCase
from diseases.models import Disease
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

# ===============================
# AI DIAGNOSIS RESULTS
# ===============================

class AIDiagnosis(models.Model):
    patient_case = models.ForeignKey(PatientCase,on_delete=models.CASCADE,related_name="diagnosis")
    disease = models.ManyToManyField(Disease,on_delete=models.CASCADE,related_name="diagnosis")
    confidence_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    explanation = models.TextField(blank=True, null=True)
    rank = models.PositiveIntegerField()

    class Meta:
        unique_together = [['patient_case', 'disease']]
        ordering = ['patient_case', 'rank']
