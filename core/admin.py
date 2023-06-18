from django.contrib import admin
# Register your models here.
from .models import Occurrence

@admin.register(Occurrence)
class OccurrenceAdmin(admin.ModelAdmin):
    list_display = ( 'date', 'profile', 'risk', 'unit_type', 'type_of_occurrence', 'type_of_traffic_accident')
    search_fields = ('id', 'date', 'risk')
