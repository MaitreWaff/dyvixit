from django import forms
from dyvixitsolutions.models import Client

class PersonForm(forms.Form):
    first  = forms.CharField()
    last   = forms.CharField()
    middle = forms.CharField()

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client