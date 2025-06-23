from django.db import models
from django.db import models
from diseases.models import Disease

# Create your models here.

class Prevention(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class DiseasePrevention(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='preventions')
    prevention = models.ForeignKey(Prevention, on_delete=models.CASCADE)

    def __str__(self):
        return self.disease.name + "-" + self.prevention.name
    class Meta:
        unique_together = [['disease', 'prevention']]