from django.contrib import admin
# Register your models here.
from .models import Profile, Gender

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'age', 'gender')
    search_fields = ('gender', 'age')

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
