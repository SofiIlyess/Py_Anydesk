from django.contrib import admin
from .models import Client,ClientsImport

# Register your models here.
admin.site.register(Client)

class ClientsImportAdmin(admin.ModelAdmin):
    list_display = ("owner","date","file")

admin.site.register(ClientsImport,ClientsImportAdmin)