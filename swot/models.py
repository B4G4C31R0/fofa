from django.db import models

# Create your models here.


class Planejamento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150, blank=True, null=True)
    lider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='lider_rel')
    membros = models.ManyToManyField('users.User', blank=True, null=True, related_name='membros_rel')
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Elementos(models.Model):
    planejamento = models.ForeignKey('Planejamento', on_delete=models.CASCADE, blank=True, null=True)
    tipo_elemento = models.CharField(max_length=20)
    descricao = models.TextField(blank=True, null=True)
    lider = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.tipo_elemento


class Fatores(models.Model):
    planejamento = models.ForeignKey('Planejamento', on_delete=models.CASCADE, blank=True, null=True)
    elemento = models.ForeignKey('Elementos', on_delete=models.CASCADE)
    descricao = models.TextField()
    criador = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.descricao


class Objetivo(models.Model):
    fator=models.ForeignKey('Fatores', on_delete=models.CASCADE, null=True)
    descricao = models.TextField()
    concluido = models.BooleanField(default=False)
    criador = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.descricao)