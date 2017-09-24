from cuser.models import CUser as User
from django.db import models

# Create your models here.
from core.utils import LIST_EXPERIENCIA, LIST_ESCOLARIDADE, DEFAULT


class Candidate(models.Model):
    user = models.ForeignKey(User)
    salario = models.DecimalField('Salario Pretenido', decimal_places=2, max_digits=10)
    experiencia = models.PositiveIntegerField('Experiencia', choices=LIST_EXPERIENCIA, default=DEFAULT)
    escolaridade = models.PositiveIntegerField('Escolaridade', choices=LIST_ESCOLARIDADE, default=DEFAULT)

    def __str__(self):
        if self.user.get_full_name() == '':
            return self.user.email
        return self.user.email

    class Meta:
        verbose_name = 'Candidatos'
        verbose_name_plural = 'Candidatos'


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
