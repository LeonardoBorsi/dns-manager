from django import forms
from .models import Domain, SubDomain, TLD

class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ['ip_address', 'names', 'TLD']


class SubDomainForm(forms.ModelForm):
    class Meta:
        model = SubDomain
        fields = ['ip_address', 'names']


class TLDForm(forms.ModelForm):
    class Meta:
        model = TLD
        fields = ['name']