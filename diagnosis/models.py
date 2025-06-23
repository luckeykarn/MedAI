from django.db import models

# Create your models here.

# ===============================
# AI DIAGNOSIS RESULTS
# ===============================

class AIDiagnosis(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    confidence_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    explanation = models.TextField(blank=True, null=True)
    rank = models.PositiveIntegerField()

    class Meta:
        unique_together = [['patient_case', 'disease']]
        ordering = ['patient_case', 'rank']
