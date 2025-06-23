from django.contrib import admin
from .models import Treatment,DiseaseTreatment
# Register your models here.

admin.site.register([Treatment,DiseaseTreatment])
