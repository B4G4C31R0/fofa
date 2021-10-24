from django.contrib import admin
from .models import *

# Register your models here.


class PlanejamentoAdmin(admin.ModelAdmin):
    list_display = ['titulo','lider','id']


class ElementoAdmin(admin.ModelAdmin):
    list_display = ['lider','planejamento','tipo_elemento','id']


class FatorAdmin(admin.ModelAdmin):
    list_display = ['descricao','criador','elemento','id',]


class ObjetivoAdmin(admin.ModelAdmin):
    list_display = ['criador','descricao','fator','elemento','concluido','id',]


class ComentarioFatorAdmin(admin.ModelAdmin):
    list_display = ['comentario','membro','fator','horario']


class ComentarioObjetivoAdmin(admin.ModelAdmin):
    list_display = ['comentario','membro','objetivo']
    

# class Admin(admin.ModelAdmin):
#     list_display = ['id',]

admin.site.register(Planejamento, PlanejamentoAdmin)
admin.site.register(Elementos, ElementoAdmin)
admin.site.register(Fatores, FatorAdmin)
admin.site.register(Objetivo, ObjetivoAdmin)
admin.site.register(ComentarioFator, ComentarioFatorAdmin)
admin.site.register(ComentarioObjetivo, ComentarioObjetivoAdmin)