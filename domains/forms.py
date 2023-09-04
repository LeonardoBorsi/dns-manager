from django import forms
from .models import Domain, SubDomain, TLD
from django.core.validators import validate_ipv4_address, RegexValidator, ValidationError

def validate_domain_names(value):
    domain_name_validator = RegexValidator(
        r'^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?$',
        'Invalid domain name.'
    )
    
    names = value.split(";")
    
    for name in names:
        try:
            domain_name_validator(name)
        except ValidationError:
            raise ValidationError("Invalid domain names")
    
class DomainForm(forms.ModelForm):
    ip_address = forms.CharField(validators=[validate_ipv4_address])
    names = forms.CharField(validators=[validate_domain_names])
    class Meta:
        model = Domain
        fields = ['ip_address', 'names', 'TLD']


class SubDomainForm(forms.ModelForm):
    ip_address = forms.CharField(validators=[validate_ipv4_address])
    names = forms.CharField(validators=[validate_domain_names])
    class Meta:
        model = SubDomain
        fields = ['ip_address', 'names']


class TLDForm(forms.ModelForm):
    class Meta:
        model = TLD
        fields = ['name']