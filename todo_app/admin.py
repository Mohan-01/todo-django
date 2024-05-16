from django.contrib import admin
from . import models

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'dead_line', 'completed', 'created_at')
    
admin.site.register(models.Task, TaskAdmin)