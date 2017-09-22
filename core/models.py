from django.db import models
from cuser.models import CUser as User
from django.shortcuts import resolve_url as r
from core.utils import LIST_EXPERIENCIA, LIST_ESCOLARIDADE, SEIS_MESES, SUPERIOR_COMPLETO


# Create your models here.

class Company(models.Model):
    name = models.CharField('Empresa', max_length=100)
    # address = models.OneToOneField('Address')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Job(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField('Vaga', max_length=100)
    description = models.TextField('Description')
    salario_min = models.DecimalField('Salario Minimo', max_digits=10, decimal_places=2)
    salario_max = models.DecimalField('Salario Max', max_digits=10, decimal_places=2)
    experiencia = models.PositiveIntegerField('Experiencia', choices=LIST_EXPERIENCIA, default=SEIS_MESES)
    escolaridade = models.PositiveIntegerField('Escolaridade', choices=LIST_ESCOLARIDADE, default=SUPERIOR_COMPLETO)
    distancia_max = models.IntegerField('D. Maxima')

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('core:job_detail', pk=self.pk)


class Candidate(models.Model):
    user = models.ForeignKey(User)
    salario = models.DecimalField('Salario Pretenido', decimal_places=2, max_digits=10)
    experiencia = models.PositiveIntegerField('Experiencia', choices=LIST_EXPERIENCIA, default=SEIS_MESES)
    escolaridade = models.PositiveIntegerField('Escolaridade', choices=LIST_ESCOLARIDADE, default=SUPERIOR_COMPLETO)

    def __str__(self):
        if self.user.get_full_name() == '':
            return self.user.email
        return self.user.email

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'


class Address(models.Model):

    logradouro = models.CharField('Logradouro', max_length=50)
    endereco = models.CharField('Endereco', max_length=60)
    numero = models.PositiveIntegerField("Numero")
    complemento = models.CharField('Complemento', max_length=40, null=True, blank=True)
    cep = models.CharField('Cep', max_length=11)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    uf = models.CharField('UF', max_length=20)
    observacao = models.TextField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return '{0} {1}, Numero {2}'.format(
            self.logradouro, self.endereco, self.numero
        ).upper()

    class Meta:
        ordering = ['-id']
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'
