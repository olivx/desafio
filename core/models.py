# -*- coding: utf-8 -*-
from django.db import models
from cuser.models import CUser as User

# Create your models here.
from company.models import Company


class Address(models.Model):
    company = models.OneToOneField(Company, null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True)
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

    def __unicode__(self):
        return '{0} {1}, Numero {2}'.format(
            self.logradouro, self.endereco, self.numero
        ).upper().encode('utf-8')

    def get_full_address(self):
        end = u'{0} {1} {2} {3} {4} {5}'.format(self.logradouro, self.endereco,
                                          self.bairro, self.bairro, self.cidade, self.uf).encode('utf-8')
        return end

    class Meta:
        ordering = ['-id']
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'
