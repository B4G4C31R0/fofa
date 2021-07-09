from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

app_name= 'swot'

lista_fofa = ['Forças','Oportunidades','Fraquezas','Ameaças']
# Create your views here.

@login_required
def home(request):
    plan = Planejamento.objects.filter(lider=request.user)
    
    return render(request, 'swot/home.html', {'plan':plan})


@login_required
def planejamento(request, id):
    elementos= Elementos.objects.filter(planejamento=id)
    return render(request, 'swot/planejamento.html', {'elementos':elementos})


def elementos(request, id):
    fatores=Fatores.objects.filter(tipo=id)
    elemento=Elementos.objects.get(id=id)
    return render(request, 'swot/elementos.html', {'fatores':fatores, 'elemento':elemento})


def adicionar_fatores(request, id):
    elemento=Elementos.objects.get(id=id)
    form=FatoresForm(request.POST or None)
    if form.is_valid():
        add_fat=form.save(commit=False)
        add_fat.tipo = elemento
        add_fat.save()
        return redirect('swot:elementos', id)
    else:
        return render(request,'swot/adicionar_fatores.html', {'form':form})


def adicionar_planejamento(request):
    usuario=request.user
    form=PlanejamentoForm(request.POST or None)
    if form.is_valid():
        plan=form.save(commit=False)
        plan.lider = usuario
        plan.save()
        for i in range(4):
            element= Elementos()
            element.planejamento=plan
            element.tipo_elemento = lista_fofa[i]
            element.save()
        return redirect('swot:home')
    else:
        return render(request,'swot/adicionar_planejamento.html', {'form':form})