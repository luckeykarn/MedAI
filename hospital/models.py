from django.db import models

# Create your models here.

# ===============================
# HOSPITALS & DOCTORS
# ===============================

class Hospital(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField("media/hospital")

    def __str__(self):
        return self.name
