from django.db import models
from diseases.models import Disease

# Create your models here.
class TreatmentsPrevention(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    treatment_1 = models.CharField(max_length=255, blank=True, null=True)
    treatment_2 = models.CharField(max_length=255, blank=True, null=True)
    treatment_3 = models.CharField(max_length=255, blank=True, null=True)
    prevention_1 = models.CharField(max_length=255, null=True, blank=True)
    prevention_2 = models.CharField(max_length=255, null=True, blank=True)
    prevention_3 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Treatment and Prevention for {self.disease.name}"
