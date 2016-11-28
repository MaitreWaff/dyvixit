from django import forms
from dyvixitsolutions.models import Client, Facture, LigneCommandeMateriel, LigneCommandeService, \
    CategoryMateriel, CategoryService

class PersonForm(forms.Form):
    first  = forms.CharField()
    last   = forms.CharField()
    middle = forms.CharField()

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture

class LigneCommandeMaterielForm(forms.ModelForm):
    class Meta:
        model = LigneCommandeMateriel

class LigneCommandeServiceForm(forms.ModelForm):
    class Meta:
        model = LigneCommandeService

