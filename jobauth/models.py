from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from jobconvo import settings


class Profile(models.Model):
    COMPANY = 1
    EMPLOYEE = 2
    KIND_USER = (
        (COMPANY, _('add job vacancy')),
        (EMPLOYEE, _('candidate job vacancy')),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    kind = models.PositiveIntegerField(_('Kind'), choices=KIND_USER, default=2)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
