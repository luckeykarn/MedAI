from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator







# ===============================
# DISEASE MODEL
# ===============================

class Disease(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    ontology_description = models.TextField(blank=True, null=True)
    uniprot_description = models.TextField(blank=True, null=True)

    # External identifiers
    mondo_id = models.CharField(max_length=50, blank=True, null=True, unique=True)
    icd_10_code = models.CharField(max_length=20, blank=True, null=True)
    icd_11_code = models.CharField(max_length=20, blank=True, null=True)

    # Scientific associations
    protein_count = models.PositiveIntegerField(default=0)
    direct_association_count = models.PositiveIntegerField(default=0)

    # Clinical flags
    is_rare = models.BooleanField(default=False)
    is_chronic = models.BooleanField(default=False)
    is_hereditary = models.BooleanField(default=False)
    is_contagious = models.BooleanField(default=False)

    # AI diagnostic metadata
    severity_level = models.CharField(
        max_length=20,
        choices=[
            ('mild', 'Mild'),
            ('moderate', 'Moderate'),
            ('severe', 'Severe'),
            ('critical', 'Critical'),
            ('variable', 'Variable'),
        ],
        default='moderate'
    )
    typical_age_onset = models.CharField(
        max_length=20,
        choices=[
            ('infancy', 'Infancy'),
            ('childhood', 'Childhood'),
            ('adolescence', 'Adolescence'),
            ('adult', 'Adult'),
            ('middle_age', 'Middle Age'),
            ('elderly', 'Elderly'),
            ('any_age', 'Any Age'),
        ],
        default='any_age'
    )
    gender_prevalence = models.CharField(
        max_length=20,
        choices=[
            ('male', 'More Common in Males'),
            ('female', 'More Common in Females'),
            ('equal', 'Equal Prevalence'),
        ],
        default='equal'
    )
    diagnostic_confidence_threshold = models.FloatField(
        default=0.7,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text="Minimum AI confidence to recommend this disease"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['is_chronic', 'is_rare']),
            models.Index(fields=['severity_level']),
        ]

    def __str__(self):
        return self.name
