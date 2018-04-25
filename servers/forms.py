from django import forms

from .models import Server1C


class Server1CForm(forms.ModelForm):
    class Meta:
        model = Server1C
        fields = ['name', 'description', 'port']