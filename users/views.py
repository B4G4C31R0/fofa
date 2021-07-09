from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import *


app_name = 'users'
# Create your views here.


def registro(request):
    form= RegistroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('swot:home')
    else:
        return render(request, 'users/registro.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('/users/login')
