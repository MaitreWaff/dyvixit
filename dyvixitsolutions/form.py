from django import forms
from dyvixitsolutions.models import Client, Facture, LigneCommandeMateriel, LigneCommandeService, \
    CategoryMateriel, CategoryService, Materiel, Service

class PersonForm(forms.Form):
    societe   = forms.CharField() # widget=forms.CheckboxInput)
    prenom    = forms.CharField()
    nom       = forms.CharField()
    fonction  = forms.CharField()
    phone     = forms.IntegerField()
    email     = forms.EmailField()
    address   = forms.CharField(widget=forms.Textarea)


class ClientForm(forms.ModelForm):
    # model = Client
    class Meta:
        model = Client

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture

    def __init__(self, *args, **kwargs):
        super(FactureForm, self).__init__(*args, **kwargs)

class LigneCommandeMaterielForm(forms.Form): #.ModelForm):
    lcm = forms.ModelMultipleChoiceField(required=False, queryset=Materiel.objects.all(), widget=forms.CheckboxSelectMultiple)
    # class Meta:
    #     model = LigneCommandeMateriel
    #
    # def __init__(self, *args, **kwargs):
    #     super(LigneCommandeMaterielForm, self).__init__(*args, **kwargs)

class LigneCommandeServiceForm(forms.Form):
    lcs = forms.ModelMultipleChoiceField(required=False, queryset=Service.objects.all(), widget=forms.CheckboxSelectMultiple)
    # class Meta:
    #     model = LigneCommandeService
    #
    # def __init__(self, *args, **kwargs):
    #     super(LigneCommandeServiceForm, self).__init__(*args, **kwargs)
