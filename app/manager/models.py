from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=200, verbose_name='Name')
    email = models.EmailField(max_length=200, verbose_name='E-mail', unique=True)
    department = models.CharField(max_length=50, verbose_name='Department')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name


class Feira(models.Model):
    longi = models.CharField(max_length=15, blank=True, default='')
    lat = models.CharField(max_length=15, blank=True, default='')
    setcens = models.CharField(max_length=20, blank=True, default='')
    areap = models.CharField(max_length=20, blank=True, default='')
    coddist = models.IntegerField(blank=True, null=True)
    distrito = models.CharField(max_length=20, blank=True, default='')
    codsubpref = models.IntegerField(blank=True, null=True)
    subprefe = models.CharField(max_length=40, blank=True, default='')
    regiao5 = models.CharField(max_length=20, blank=True, default='')
    regiao8 = models.CharField(max_length=20, blank=True, default='')
    nome_feira = models.CharField(max_length=40, blank=True, default='')
    registro = models.CharField(max_length=10, blank=True, default='')
    logradouro = models.CharField(max_length=40, blank=True, default='')
    numero = models.CharField(max_length=15, blank=True, default='')
    bairro = models.CharField(max_length=40, blank=True, default='')
    referencia = models.CharField(max_length=40, blank=True, default='')

    class Meta:
        verbose_name = 'Feira'
        verbose_name_plural = 'Feiras'

    def __str__(self):
        return 'nome: {}, bairro: {}'.format(self.nome_feira, self.bairro)
