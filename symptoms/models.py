from django.db import models
from diseases.models import Disease
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
# ===============================
# CORE MEDICAL ENTITIES
# ===============================

class Symptom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    is_emergency = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
# ===============================
# RELATIONSHIPS
# ===============================

class DiseaseSymptom(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='symptoms')
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    frequency_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],null=True,blank = True) # 90% of patients with Type 2 Diabetes have this symptom
    specificity_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],null=True,blank = True) # The symptom is highly specific to this disease

    class Meta:
        unique_together = [['disease', 'symptom']]
