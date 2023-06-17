from django.contrib import admin
# Register your models here.
from .models import Occurrence

@admin.register(Occurrence)
class OccurrenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'risk')
    search_fields = ('id', 'date', 'risk')

