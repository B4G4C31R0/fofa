from django import forms
from .models import *


class FatoresForm(forms.ModelForm):
    class Meta:
        model= Fatores
        fields= ('descricao',)


class PlanejamentoForm(forms.ModelForm):
    class Meta:
        model = Planejamento
        fields = ('titulo','descricao')


class ObjetivoForm(forms.ModelForm):
    class Meta:
        model= Objetivo
        fields= ('descricao',)


class ObjetivoConcluidoForm(forms.ModelForm):
    class Meta:
        model= Objetivo
        fields= ('descricao','concluido')