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
    a=12
    return render(request, 'base.html',{'a':a})


@login_required
def home(request):
    membro = Membro.objects.get(usuario=request.user)
    conv = Convite.objects.filter(convidado = membro)
    plan = Planejamento.objects.filter(membros = membro)
    return render(request, 'swot/home.html', {'plan':plan, 'membro':membro, 'conv':conv})


@login_required
def elementos(request, id):
    plan = Planejamento.objects.get(id=id)
    elementos= Elementos.objects.filter(planejamento=plan)
    fatores = Fatores.objects.filter(planejamento = plan)
    return render(request, 'swot/elementos.html', {'elementos':elementos, 'plan':plan, 'fatores':fatores})


def fatores(request, id):
    elemento=Elementos.objects.get(id=id)
    fatores=Fatores.objects.filter(elemento=elemento)
    objetivos = Objetivo.objects.filter(elemento=elemento)
    return render(request, 'swot/fatores.html',{'elemento':elemento,'fatores':fatores, 'objetivos':objetivos})


def objetivo(request, id):
    objetivo=Objetivo.objects.get(id=id)
    form = ObjetivoConcluidoForm(request.POST or None, instance=objetivo)
    if form.is_valid():
        form.save()
        return redirect('swot:fatores', objetivo.fator.elemento.id)
    else:
        return render(request, 'swot/objetivo.html',{'objetivo':objetivo, 'form':form})


def editarMembro(request, id_plan, id_memb):
    plan = Planejamento.objects.get(id=id_plan)
    elementos = Elementos.objects.filter(planejamento = plan)
    membro = Membro.objects.get(id = id_memb)
    
    if request.method == "POST":
        forca = request.POST.get('força', 'Nao encontrado')
        oport = request.POST.get('oport', 'Nao encontrado')
        fraq = request.POST.get('fraq', 'Nao encontrado')
        ameac = request.POST.get('ameac', 'Nao encontrado')

        fo = elementos[0]
        op = elementos[1]
        fr = elementos[2]
        am = elementos[3]
    
        if forca == 'on':
            fo.member.add(membro)
            fo.save()
        else:
            fo.member.remove(membro)
            fo.save()

        if oport == 'on':
            op.member.add(membro)
            op.save()
        else:
            op.member.remove(membro)
            op.save()

        if fraq == 'on':
            fr.member.add(membro)
            fr.save()
        else:
            fr.member.remove(membro)
            fr.save()

        if ameac == 'on':
            am.member.add(membro)
            am.save()
        else:
            am.member.remove(membro)
            am.save()

    return render(request, 'swot/editarMembro.html', {'plan':plan, 'membro':membro, 'elementos':elementos})


def adicionar_fatores(request, id):
    membro = Membro.objects.get(usuario = request.user)
    elemento=Elementos.objects.get(id=id)
    form=FatoresForm(request.POST or None)
    if form.is_valid():
        add_fat=form.save(commit=False)
        add_fat.planejamento = elemento.planejamento
        add_fat.criador = membro
        add_fat.elemento = elemento
        add_fat.save()
        return redirect('swot:fatores', id)
    else:
        return render(request,'swot/adicionar_fatores.html', {'form':form, 'elemento':elemento})


def editarFator(request, id):
    fator = Fatores.objects.get(id=id)
    form = FatoresForm(request.POST or None, instance=fator)
    coment = ComentarioFator.objects.filter(fator=fator)
    if form.is_valid():
        form.save()
        return redirect('swot:fatores', fator.elemento.id)
    else:
        return render(request, 'swot/editarFator.html', {'fator':fator, 'form':form, 'coment':coment})


def adicionar_objetivo(request, id):
    membro = Membro.objects.get(usuario = request.user)
    fator=Fatores.objects.get(id=id)
    form = ObjetivoForm(request.POST or None)
    if form.is_valid():
        add_obj = form.save(commit=False)
        add_obj.criador = membro
        add_obj.fator = fator
        add_obj.elemento = fator.elemento
        add_obj.concluido = False
        add_obj.save()
        return redirect('swot:fatores', fator.elemento.id)
    else:
        return render(request,'swot/adicionar_objetivo.html', {'form':form, 'fator':fator})


# def adicionar_planejamento(request):
#     membro=Membro.objects.get(usuario=request.user)
#     form=PlanejamentoForm(request.POST or None)
#     if form.is_valid():
#         plan=form.save(commit=False)
#         plan.lider = membro
#         plan.save()
#         plan.membros.add(membro)
#         plan.save()
#         for i in range(4):
#             element= Elementos()
#             element.planejamento=plan
#             element.tipo_elemento = lista_fofa[i]
#             element.descricao = desc_fofa[i]
#             element.save()
#         conv = Convite()
#         conv.planejamento = plan
#         conv.lider = membro
#         conv.save()
#         return redirect('swot:home')
#     else:
#         return render(request,'swot/adicionar_planejamento.html', {'form':form})

def adicionar_planejamento(request):
    membro=Membro.objects.get(usuario=request.user)
    if request.method == "POST":
        plan=Planejamento()
        plan.titulo = request.POST['titulo']
        plan.descricao = request.POST['descricao']
        plan.lider = membro
        plan.save()
        plan.membros.add(membro)
        plan.save()
        for i in range(4):
            element= Elementos()
            element.planejamento=plan
            element.tipo_elemento = lista_fofa[i]
            element.descricao = desc_fofa[i]
            element.save()
        conv = Convite()
        conv.planejamento = plan
        conv.lider = membro
        conv.save()
        return redirect('swot:home')
    else:
        return render(request,'swot/adicionar_planejamento.html')


def liderElemento(request, membro, id):
    elemento = Elementos.objects.get(id=id)
    membro = Membro.objects.get(id=membro)

    if elemento.lider != None:
        print('tem gente')
        elemento.lider = membro
        elemento.save()
    else:
        print('tem gente n')
        elemento.lider = membro
        elemento.save()

    return redirect ('swot:elementos', elemento.planejamento.id)


def comentarioFator(request, id):
    membro = Membro.objects.get(usuario = request.user)
    fator = Fatores.objects.get(id=id)
    form = ComentarioFator()
    if request.method == "POST":
        form.comentario = request.POST['message']
        form.fator = fator
        form.membro = membro
        form.save()
    return redirect('swot:editarFator', id)


def teste(request):
    return render(request, 'swot/teste.html')