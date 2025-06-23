from django.contrib import admin
from .models import Prevention,DiseasePrevention
# Register your models here.
admin.site.register([Prevention,DiseasePrevention])
