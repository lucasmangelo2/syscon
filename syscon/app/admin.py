from django.contrib import admin
from .models import Function, Collaborator, Apartament, Resident

# Register your models here.

admin.site.register(Function)
admin.site.register(Collaborator)
admin.site.register(Apartament)
admin.site.register(Resident)