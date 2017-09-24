from django.db import models
from cuser.models import CUser as User
from django.shortcuts import resolve_url as r

# Create your models here.
from core.utils import LIST_EXPERIENCIA, LIST_ESCOLARIDADE, DEFAULT


class Company(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField('Empresa', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Job(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField('Vaga', max_length=100)
    description = models.TextField('Description')
    salario_min = models.DecimalField('Salario Minimo', max_digits=10, decimal_places=2)
    salario_max = models.DecimalField('Salario Max', max_digits=10, decimal_places=2)
    experiencia = models.PositiveIntegerField('Experiencia', choices=LIST_EXPERIENCIA, default=DEFAULT)
    escolaridade = models.PositiveIntegerField('Escolaridade', choices=LIST_ESCOLARIDADE, default=DEFAULT)
    distancia_max = models.IntegerField('D. Maxima')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return r('core:job_detail', pk=self.pk)
