from django import forms

class PersonForm(forms.Form):
    first  = forms.CharField()
    last   = forms.CharField()
    middle = forms.CharField()