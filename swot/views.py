from fofa.settings import ALLOWED_HOSTS
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import *
from users.models import *
from .forms import *

app_name= 'swot'

lista_fofa = ['Forças','Oportunidades','Fraquezas','Ameaças']
desc_fofa = [
    'Representa as qualidades positivas da empresa, ou seja, tudo aquilo que agrega valores e está sob o controle da organização.',
    'São fatores externos (que não estão sob a influência da empresa) e quando surgem, trazem benefícios para a corporação. EX: uma nova lei que possa beneficiar a empresa de algum modo.',
    'São pontos que atrapalham e não trazem vantagens competitivas para a corporação. Assim como as Forças, as Fraquezas também estão sob o comando da empresa.',
    'Também não estão sob o controle da empresa, porém são fatores que podem prejudicar a corporação de algum modo. Um exemplo pode ser a entrada de uma grande empresa no segmento.'
]
# Create your views here.


def base(request):
    return render(request, 'base.html')


@login_required
def home(request):
    plan = Planejamento.objects.filter(lider=request.user)
    
    return render(request, 'swot/home.html', {'plan':plan})


@login_required
def elementos(request, id):
    plan = Planejamento.objects.get(id=id)
    membros = Membro.objects.filter(planejamento=plan)
    elementos= Elementos.objects.filter(planejamento=id)
    fatores = Fatores.objects.all()
    return render(request, 'swot/elementos.html', {'elementos':elementos, 'plan':plan, 'fatores':fatores, 'membros':membros})


def fatores(request, id):
    elemento=Elementos.objects.get(id=id)
    fatores=Fatores.objects.filter(elemento=elemento)
    objetivos = Objetivo.objects.all()
    return render(request, 'swot/fatores.html',{'elemento':elemento,'fatores':fatores, 'objetivos':objetivos})


def objetivo(request, id):
    objetivo=Objetivo.objects.get(id=id)
    form = ObjetivoConcluidoForm(request.POST or None, instance=objetivo)
    if form.is_valid():
        form.save()
        return redirect('swot:fatores', objetivo.fator.elemento.id)
    else:
        return render(request, 'swot/objetivo.html',{'objetivo':objetivo, 'form':form})


def adicionar_fatores(request, id):
    elemento=Elementos.objects.get(id=id)
    form=FatoresForm(request.POST or None)
    if form.is_valid():
        add_fat=form.save(commit=False)
        add_fat.planejamento = elemento.planejamento
        add_fat.criador = request.user
        add_fat.elemento = elemento
        add_fat.save()
        return redirect('swot:fatores', id)
    else:
        return render(request,'swot/adicionar_fatores.html', {'form':form})


def adicionar_objetivo(request, id):
    fator=Fatores.objects.get(id=id)
    form = ObjetivoForm(request.POST or None)
    if form.is_valid():
        add_obj = form.save(commit=False)
        add_obj.criador = request.user
        add_obj.fator = fator
        add_obj.concluido = False
        add_obj.save()
        return redirect('swot:fatores', fator.elemento.id)
    else:
        return render(request,'swot/adicionar_objetivo.html', {'form':form})


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
            element.descricao = desc_fofa[i]
            element.save()
        return redirect('swot:home')
    else:
        return render(request,'swot/adicionar_planejamento.html', {'form':form})




def teste(request):
    return render(request, 'swot/teste.html')