from django.db import models
from django.db import models
from diseases.models import Disease
# Create your models here.

class Treatment(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class DiseaseTreatment(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='treatments')
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['disease', 'treatment']]