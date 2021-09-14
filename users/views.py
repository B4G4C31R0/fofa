from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.core import serializers
import json

from swot.models import *
from .models import *
from .forms import *

app_name = 'users'
# Create your views here.


def adicionar_membros(request, id):
    conv = Convite.objects.filter(planejamento = id)
    plan=Planejamento.objects.get(id=id)
    pesquisa = request.GET.get('pesquisa', None)

    if pesquisa:
        usuarios = User.objects.filter(first_name__icontains=pesquisa) # ao colocar '__icontains=' no final, serve para ignorar se a letra é maiuscula ou minuscula
    else:
        usuarios = User.objects.all()   

    return render(request,'users/adicionar_membros.html', {'plan':plan, 'usuarios':usuarios, 'conv': conv})


def getUsuarios(request, id):
    dataM = serializers.serialize("json", Membro.objects.all(), fields=('usuario', 'nome','avatar','id'))
    dataP = serializers.serialize("json", Planejamento.objects.filter(id=id), fields=('membros'))
    dataC = serializers.serialize("json", Convite.objects.filter(planejamento=id), fields=('convidado'))
    
    j = json.loads(dataM)
    p = json.loads(dataP)
    c = json.loads(dataC)

    return JsonResponse({'membros':j, 'plan':p, 'conv':c})

    # data2 = {'membros':[]}
    # for i in j:
    #     data2['membros'].append(i)
    # print (data2)
    # return JsonResponse({'membros':list(membros.values('usuario','primeiro_nome','planejamento', 'elemento','id'))})


def add_membro(request):
    if request.method == 'POST':
        membro = Membro.objects.get(usuario=request.POST['usuario'])
        plan = Planejamento.objects.get(id=request.POST['planej'])

        plan.membros.add(membro)
        plan.save()
        return redirect('users:adicionar_membros', plan.id)



# def add_membro(request):
#     if request.method == 'POST':
#         membro = Membro.objects.get(usuario=usuario)
#         plan = Planejamento.objects.get(id=id)
        
#         membro.planejamento.add(plan)
#         membro.save()

#         plan.membros.add(usuario)
#         plan.save()
#         return redirect('users:adicionar_membros', id)


def rm_membro(request, id, usuario):
    pass





def registro(request):
    form= RegistroForm(request.POST or None)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.save()
        membro = Membro()
        membro.usuario = usuario
        membro.primeiro_nome = usuario.first_name
        membro.save()
        return redirect('swot:home')
    else:
        return render(request, 'users/registro.html', {'form':form})


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('swot:home')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'users/logar.html', {'form_login': form_login})


def logout_view(request):
    logout(request)
    return redirect('/users/login')


# CONVITES ===================================

def getConvites(request, id):
    convit = serializers.serialize("json", Convite.objects.filter(convidado=id), fields=('lider', 'convidado','planejamento','id'))
    convites = json.loads(convit)
    return JsonResponse({'convites': convites})


def convites(request, id):
    membro = Membro.objects.get(usuario=id)
    conv = Convite.objects.filter(convidado = membro)
    return render(request, 'users/convites.html', {'membro':membro, 'conv':conv})


def novoConvite(request):
    convidado = Membro.objects.get(id=request.POST['convidadoId'])
    conv = Convite.objects.get(id=request.POST['conviteId'])

    conv.convidado.add(convidado)
    conv.save()

    return redirect ('users:adicionar_membros', conv.planejamento.id)


def convAceito(request, id, idplan, conv):
    plan = Planejamento.objects.get(id=idplan)
    membro = Membro.objects.get(id=id)
    convite = Convite.objects.get(id=conv)

    convite.convidado.remove(membro)
    plan.membros.add(membro)
    plan.save()
    convite.save()

    print(convite, convite.id)

    return redirect('swot:home')


def convRecusado(request, id, membro):
    convite = Convite.objects.get(id=id)
    membr = Membro.objects.get(id=membro)
    convite.convidado.remove(membr)
    convite.save()

    return redirect('users:convites', membr.usuario.id)


# FIM DOS CONVITES ===================================


def perfil(request, id):
    membro = Membro.objects.get(usuario = id)
    form= PerfilForm(request.POST or None, instance=membro)
    if form.is_valid():
        perfil = form.save(commit=False)
        perfil.save()
        return redirect('swot:home')
    else:
        return render (request, 'users/perfil.html', {'membro':membro, 'form':form})