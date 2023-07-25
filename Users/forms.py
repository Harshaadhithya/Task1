from django.forms import ModelForm
from .models import *
from django import forms


class ImportedContactForm(ModelForm):
    class Meta:
        model = ImportedContact
        fields = ['file']

        widget={
            'file' : forms.FileInput(attrs={'accept':'application/pdf'})
            }


