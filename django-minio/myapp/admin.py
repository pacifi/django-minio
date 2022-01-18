from django.contrib import admin

from myapp.models import Persona


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass

