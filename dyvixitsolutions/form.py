from django import forms
from dyvixitsolutions.models import Client, Facture, LigneCommandeMateriel, LigneCommandeService, \
    CategoryMateriel, CategoryService

class PersonForm(forms.Form):
    societe   = forms.CharField() # widget=forms.CheckboxInput)
    prenom    = forms.CharField()
    nom       = forms.CharField()
    fonction  = forms.CharField()
    telephone = forms.IntegerField()
    email     = forms.EmailField()

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

