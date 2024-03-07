from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'uptaded') # Campos para que sean de solo lectura

admin.site.register(Project, ProjectAdmin) # Registra el modelo Project en el panel de administración de Django
