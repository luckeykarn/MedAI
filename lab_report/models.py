from django.db import models
from diseases.models import Disease

# Create your models here.
class LabReport(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)  
    jensenlab_textmining_zscore = models.FloatField(null=True, blank=True)  
    jensenlab_confidence = models.FloatField(null=True, blank=True) 
    expression_atlas_log2_fold_change = models.FloatField(null=True, blank=True) 
    disgenet_score = models.FloatField(null=True, blank=True)  
    associated_disease_evidence = models.TextField(null=True, blank=True) 
    associated_disease_drug_name = models.CharField(max_length=255, null=True, blank=True)  
    associated_disease_p_value = models.FloatField(null=True, blank=True)  
    associated_disease_source = models.CharField(max_length=255, null=True, blank=True) 
    associated_disease_source_id = models.CharField(max_length=100, null=True, blank=True) 
    monarch_s2o = models.CharField(max_length=255, null=True, blank=True)  

    def __str__(self):
        return f"Lab Report for {self.disease.name}"