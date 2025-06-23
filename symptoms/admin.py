from django.contrib import admin
from .models import Symptom,DiseaseSymptom

# Register your models here.
admin.site.register([Symptom,DiseaseSymptom])
