from django.contrib import admin

# Register your models here.
from core.forms import AddressForm
from core.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    form = AddressForm



