from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# ===============================
# HOSPITALS & DOCTORS
# ===============================

class Hospital(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100, blank=True, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.user.get_full_name() or self.user.username}"


# ===============================
# CORE MEDICAL ENTITIES
# ===============================

class Symptom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    is_emergency = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Cause(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Treatment(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Prevention(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    common_dosage = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


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


# ===============================
# RELATIONSHIPS
# ===============================

class DiseaseSymptom(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='symptoms')
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    frequency_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    specificity_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    class Meta:
        unique_together = [['disease', 'symptom']]


class DiseaseCause(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='causes')
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['disease', 'cause']]


class DiseaseTreatment(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='treatments')
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['disease', 'treatment']]


class DiseasePrevention(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='preventions')
    prevention = models.ForeignKey(Prevention, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['disease', 'prevention']]


# ===============================
# PATIENT CASES & PRESCRIPTIONS
# ===============================

class PatientCase(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('unknown', 'Unknown')
    ])
    reported_symptoms = models.ManyToManyField(Symptom, through='PatientSymptom')
    suggested_diseases = models.ManyToManyField(Disease, through='AIDiagnosis')
    is_emergency = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patient Case #{self.id}"


class PatientSymptom(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    severity = models.CharField(max_length=20, choices=[
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ])
    duration_days = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together = [['patient_case', 'symptom']]


class Prescription(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)  # e.g. "2x/day"
    duration_days = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    prescribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicine.name} for Case #{self.patient_case.id}"


# ===============================
# AI DIAGNOSIS RESULTS
# ===============================

class AIDiagnosis(models.Model):
    patient_case = models.ForeignKey(PatientCase, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    confidence_score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    explanation = models.TextField(blank=True, null=True)
    rank = models.PositiveIntegerField()

    class Meta:
        unique_together = [['patient_case', 'disease']]
        ordering = ['patient_case', 'rank']
