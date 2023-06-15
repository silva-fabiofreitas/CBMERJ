from django.contrib import admin

# Register your models here.
from .models import RiskRating, typeOfOccurrence, TypeOfTrafficAccident, UnitType

@admin.register(RiskRating)
class RiskRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating')
    search_fields = ('id', 'rating')


@admin.register(typeOfOccurrence)
class typeOfOccurrenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(TypeOfTrafficAccident)
class TypeOfTrafficAccidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')