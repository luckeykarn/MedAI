from django.contrib import admin
from .models import Cause,DiseaseCause

admin.site.register([Cause,DiseaseCause])
