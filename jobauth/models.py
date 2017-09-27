# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from cuser.models import CUser as User
from django.dispatch import receiver
from django.conf import settings
from django.db import models

# Create your models here.
from core.utils import LIST_EXPERIENCIA, DEFAULT, LIST_ESCOLARIDADE


class Profile(models.Model):
    COMPANY = 1
    EMPLOYEE = 2
    KIND_USER = (
        (COMPANY, 'Empresa'),
        (EMPLOYEE, 'Candidato'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kind = models.PositiveIntegerField('Tipo', choices=KIND_USER, default=EMPLOYEE)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class Candidate(models.Model):
    user = models.ForeignKey(User)
    last_job = models.TextField('Ultimo Emprego', null=True, blank=True)
    salario = models.DecimalField('Salario Pretenido', decimal_places=2, max_digits=10)
    experiencia = models.PositiveIntegerField('Experiencia', choices=LIST_EXPERIENCIA, default=DEFAULT)
    escolaridade = models.PositiveIntegerField('Escolaridade', choices=LIST_ESCOLARIDADE, default=DEFAULT)

    def __unicode__(self):
        if self.user.get_full_name() == '':
            return self.user.email
        return self.user.email

    class Meta:
        verbose_name = 'Candidatos'
        verbose_name_plural = 'Candidatos'

