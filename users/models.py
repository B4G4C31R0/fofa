from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.

class User(AbstractUser):

    def __str__(self):
        return self.username


class Membro(models.Model):
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)
    primeiro_nome = models.CharField(max_length=100, blank=True, null=True)
    ultimo_nome = models.CharField(max_length=100, blank=True, null=True)

    avatar= models.ImageField(upload_to='perfil_pics',blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True, unique=True)
    instagram = models.CharField(max_length=100, blank=True, null=True, unique=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True, unique=True)
    twitter = models.CharField(max_length=100, blank=True, null=True, unique=True)
    git = models.CharField(max_length=100, blank=True, null=True, unique=True)

    planejamento = models.ManyToManyField('swot.Planejamento', blank=True, null=True, related_name='plan_rel')
    elemento = models.ManyToManyField('swot.Elementos', blank=True, null=True)
    lider_elemento = OneToOneField('swot.Elementos',on_delete=models.CASCADE,blank=True, null=True, related_name='lider_elem_rel')
    lider_objetivo = models.ManyToManyField('swot.Objetivo', blank=True, null=True, related_name='obj_rel')

    def __str__(self):
        return str(self.usuario)