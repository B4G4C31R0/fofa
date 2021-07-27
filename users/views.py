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
    plan=Planejamento.objects.get(id=id)
    pesquisa = request.GET.get('pesquisa', None)

    if pesquisa:
        usuarios = User.objects.filter(first_name__icontains=pesquisa) # ao colocar '__icontains=' no final, serve para ignorar se a letra é maiuscula ou minuscula
    else:
        usuarios = User.objects.all()   

    return render(request,'swot/adicionar_membros.html', {'plan':plan, 'usuarios':usuarios, 'pesquisa':pesquisa})


def getUsuarios(request):
    membros = Membro.objects.all()
    data = serializers.serialize("json", Membro.objects.all(), fields=('usuario', 'primeiro_nome','planejamento','id'))
    
    j = eval(data)

    # data2 = {'membros':[]}
    # for i in j:
    #     data2['membros'].append(i)
    
    # print (data2)

    return JsonResponse({'membros':j})
    # return JsonResponse({'membros':list(membros.values('usuario','primeiro_nome','planejamento', 'elemento','id'))})


def add_membro(request):
    if request.method == 'POST':
        membro = Membro.objects.get(usuario=request.POST['usuario'])
        plan = Planejamento.objects.get(id=request.POST['planej'])
        
        membro.planejamento.add(plan)
        membro.save()

        plan.membros.add(request.POST['usuario'])
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
