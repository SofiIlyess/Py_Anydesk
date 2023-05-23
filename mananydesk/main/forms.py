from django import forms
from .models import ClientsImport

class ImportForm(forms.ModelForm):
    class Meta:
        model = ClientsImport
        fields = ('file',)