from django.db import models

# Create your models here.
class Disease(models.Model):
    public_id = models.CharField(max_length=100, unique=True)
    disease_name = models.CharField(max_length=255)
    disease_ontology_description = models.TextField()


class DiseaseDescription(models.Model):
    description = models.TextField()
    
    uniprot = models.CharField(max_length=255) 
    uniprot_description = models.TextField()  
    mondo_id = models.CharField(max_length=100)  # Mondo ID (disease classification)
    disease_data_source = models.CharField(max_length=255)
    associated_disease = models.CharField(max_length=255, null=True, blank=True)  
    protein_count = models.PositiveIntegerField(null=True, blank=True) 
    direct_association_count = models.PositiveIntegerField(null=True, blank=True)  
    gard_rare = models.BooleanField(default=False)  # Whether the disease is rare (GARD classification)
    symbol = models.CharField(max_length=100, null=True, blank=True)  # Gene symbol associated with the disease
    disease_ontology_url = models.URLField(null=True, blank=True)  
    mondosource_id = models.CharField(max_length=100, null=True, blank=True) 
    

    def __str__(self):
        return self.name