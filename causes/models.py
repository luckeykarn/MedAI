from django.db import models
from diseases.models import Disease

# Create your models here.
class Causes(models.Model):
    disease= models.ForeignKey(Disease, on_delete=models.CASCADE)
    causes_1 = models.CharField(max_length=255, blank=True, null=True)
    causes_2 = models.CharField(max_length=255, blank=True, null=True)
    causes_3 = models.CharField(max_length=255, blank=True, null=True)
    causes_4 = models.CharField(max_length=255, blank=True, null=True)
    causes_5 = models.CharField(max_length=255, blank=True, null=True)
    causes_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Causes of {self.disease.name}"