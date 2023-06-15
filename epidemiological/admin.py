from django.contrib import admin
# Register your models here.
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'age', 'gender')
    search_fields = ('gender', 'age')

