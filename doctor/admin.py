from django.contrib import admin
from .models import Doctor,Speciality
# Register your models here.

admin.site.register([Doctor,Speciality])
