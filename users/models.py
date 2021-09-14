from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.

class User(AbstractUser):

    def __str__(self):
        return self.username


class Membro(models.Model):
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    avatar= models.ImageField(upload_to='perfil_pics',blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name="Link do Facebook")
    instagram = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name="Link do Instagram")
    linkedin = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name="Link do Linkedin")
    twitter = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name="Link do Twitter")
    git = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name="Link do Git")

    def __str__(self):
        return str(self.usuario)


class Convite(models.Model):
    lider = models.ForeignKey('Membro', on_delete=models.CASCADE, related_name='lider')
    convidado = models.ManyToManyField('Membro', related_name='convidado', blank=True)
    planejamento = models.ForeignKey('swot.Planejamento', on_delete=models.CASCADE)
    # resolvido = models.BooleanField(default=False)

    def __str__(self):
        return str(self.lider)