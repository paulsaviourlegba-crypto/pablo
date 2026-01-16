from django.contrib import admin
from .models import JobApplication
# Register your models here.

class JobApplication(admin.ModelAdmin):
    list_display = ('full_name', 'profile_picure','resume')
    list_editable = ('full_name')

admin.site.register(JobApplication)