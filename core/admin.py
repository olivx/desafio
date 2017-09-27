from django.contrib import admin

# Register your models here.
from core.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    search_fields = ('user','user__first_name', 'endereco' ,'bairro','cidade',)
    list_display = ('user','__unicode__',)

