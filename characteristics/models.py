from django.db import models
from diseases.models import Disease

# Create your models here.
class Characteristics(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)  
    severity_of_disease = models.CharField(max_length=100)  
    diagnosis_methods = models.TextField()  
    complications = models.TextField() 
    epidemiology = models.TextField() 
    prognosis = models.TextField()  

    def __str__(self):
        return f"Characteristics of {self.disease.name}"
