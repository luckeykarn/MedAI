from django.db import models
from diseases.models import Disease


# Create your models here.
class Symptom(models.Model):
    
    diseases = models.ForeignKey(Disease, on_delete=models.CASCADE)
    symptoms_1 = models.CharField(max_length=255, blank=True, null=True)
    symptoms_2 = models.CharField(max_length=255, blank=True, null=True)
    symptoms_3 = models.CharField(max_length=255, blank=True, null=True)
    symptoms_4 = models.CharField(max_length=255, blank=True, null=True)
    symptoms_5 = models.CharField(max_length=255, blank=True, null=True)
    symptoms_6 = models.CharField(max_length=255, blank=True, null=True)
    symptoms_7 = models.CharField(max_length=255, blank=True, null=True)
    symptoms_8 = models.CharField(max_length=255, blank=True, null=True)
    symptoms_9 = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    symptoms_description = models.TextField(blank=True, null=True)

    def __str__(self):
       return f"Symptoms of {self.disease.name}"
