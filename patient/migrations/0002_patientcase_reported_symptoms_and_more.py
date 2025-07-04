# Generated by Django 5.2.1 on 2025-06-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0001_initial'),
        ('diseases', '0001_initial'),
        ('patient', '0001_initial'),
        ('patientsymptoms', '__first__'),
        ('symptoms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientcase',
            name='reported_symptoms',
            field=models.ManyToManyField(through='patientsymptoms.PatientSymptom', to='symptoms.symptom'),
        ),
        migrations.AddField(
            model_name='patientcase',
            name='suggested_diseases',
            field=models.ManyToManyField(through='diagnosis.AIDiagnosis', to='diseases.disease'),
        ),
    ]
