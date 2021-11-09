from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegistroForm(UserCreationForm):
    class Meta:
        model= User
        fields= ('username','first_name', 'password1','password2')
    
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repita a senha'


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields=('nome', 'id')