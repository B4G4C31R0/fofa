from django.contrib import admin
from .models import *

# Register your models here.

class ElementoAdmin(admin.ModelAdmin):
    list_display = ['planejamento','tipo_elemento']

admin.site.register(Planejamento)
admin.site.register(Elementos, ElementoAdmin)
admin.site.register(Projeto)
admin.site.register(Fatores)
admin.site.register(Objetivo)