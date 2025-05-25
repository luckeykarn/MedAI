from django.db import models
from diseases.models import Disease

# Create your models here.
class RiskFactor(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)  
    risk_factor = models.TextField()  
    age_of_onset = models.PositiveIntegerField()  
    genetic_factors = models.TextField()  
    family_history = models.TextField()  

    def __str__(self):
        return f"Risk Factors for {self.disease.name}"

