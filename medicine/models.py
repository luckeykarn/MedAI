from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    common_dosage = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name