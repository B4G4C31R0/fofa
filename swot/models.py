from django.db import models
from datetime import date
# Create your models here.


class Planejamento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150, blank=True, null=True)
    lider = models.ForeignKey('users.Membro', on_delete=models.CASCADE, related_name='plan_lider_rel')
    membros = models.ManyToManyField('users.Membro', blank=True, null=True, related_name='plan_membros_rel')
    prazo = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    @property
    def prazo_final(self):
        return date.today() < self.prazo


class Elementos(models.Model):
    planejamento = models.ForeignKey('Planejamento', on_delete=models.CASCADE, blank=True, null=True)
    tipo_elemento = models.CharField(max_length=20)
    descricao = models.TextField(blank=True, null=True)
    lider = models.ForeignKey('users.Membro', on_delete=models.CASCADE, blank=True, null=True)
    member = models.ManyToManyField('users.Membro', blank=True, null=True, related_name='elementos_membros_rel')

    def __str__(self):
        return self.tipo_elemento


class Fatores(models.Model):
    planejamento = models.ForeignKey('Planejamento', on_delete=models.CASCADE, blank=True, null=True)
    elemento = models.ForeignKey('Elementos', on_delete=models.CASCADE)
    descricao = models.TextField()
    criador = models.ForeignKey('users.Membro', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.descricao


class Objetivo(models.Model):
    elemento = models.ForeignKey('Elementos', on_delete=models.CASCADE, blank=True, null=True)
    fator=models.ForeignKey('Fatores', on_delete=models.CASCADE, null=True)
    descricao = models.TextField()
    concluido = models.BooleanField(default=False)
    criador = models.ForeignKey('users.Membro', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.descricao)


class ComentarioFator(models.Model):
    fator = models.ForeignKey('Fatores', on_delete=models.CASCADE)
    membro = models.ForeignKey('users.Membro', on_delete=models.CASCADE)
    comentario = models.TextField()
    horario = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.comentario


class ComentarioObjetivo(models.Model):
    objetivo = models.ForeignKey('Objetivo', on_delete=models.CASCADE)
    membro = models.ForeignKey('users.Membro', on_delete=models.CASCADE)
    comentario = models.TextField()
    horario = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.comentario
