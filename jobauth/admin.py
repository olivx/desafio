from cuser.admin import UserAdmin
from cuser.models import CUser as User
from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from jobauth.forms import CandidateForm
from jobauth.models import Profile, Candidate


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    form = CandidateForm


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)