from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from cuser.models import CUser as User
from django.dispatch import receiver
from django.conf import settings
from django.db import models

# Create your models here.


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
