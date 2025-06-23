from django.db import models
from diseases.models import Disease

# Create your models here.
class Cause(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class DiseaseCause(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='causes')
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)

    def __str__(self):
        return self.disease.name + "-" + self.cause.name
    class Meta:
        unique_together = [['disease', 'cause']]