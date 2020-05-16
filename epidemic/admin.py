from django.contrib import admin
from .models import Country, DailyInfectionScan

admin.site.register(Country)
admin.site.register(DailyInfectionScan)
