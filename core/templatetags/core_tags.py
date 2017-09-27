from cuser.models import CUser
from django import template

from company.models import Job

register = template.Library()


@register.filter
def user_job(user, users):
    return CUser.objects.get(pk=user.id)
