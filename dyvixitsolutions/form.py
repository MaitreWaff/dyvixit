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
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture

    def __init__(self, *args, **kwargs):
        super(FactureForm, self).__init__(*args, **kwargs)

class LigneCommandeMaterielForm(forms.ModelForm):
    class Meta:
        model = LigneCommandeMateriel

    def __init__(self, *args, **kwargs):
        super(LigneCommandeMaterielForm, self).__init__(*args, **kwargs)

class LigneCommandeServiceForm(forms.ModelForm):
    class Meta:
        model = LigneCommandeService

    def __init__(self, *args, **kwargs):
        super(LigneCommandeServiceForm, self).__init__(*args, **kwargs)
