from django.db import models

# Create your models here.


class Planejamento(models.Model):
    titulo = models.CharField(max_length=100)
    lider = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Elementos(models.Model):
    planejamento = models.ForeignKey('Planejamento', on_delete=models.CASCADE, blank=True, null=True)
    tipo_elemento = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_elemento


class Fatores(models.Model):
    tipo = models.ForeignKey('Elementos', on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return str(self.tipo)


class Objetivo(models.Model):
    descricao = models.TextField()
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return str(self.descricao)


class Swot(models.Model):
    pass
    # forcas = models.ManyToManyField('Elementos')
    # oportunidades = models.ManyToManyField('Elementos')
    # fraquezas = models.ManyToManyField('Elementos')
    # ameacas = models.ManyToManyField('Elementos')


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    membros = models.ManyToManyField('users.User')
    deadline = models.DateField()

    def __str__(self):
        return self.titulo
