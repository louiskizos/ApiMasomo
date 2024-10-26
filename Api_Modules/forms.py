from django import forms
from .models import *




class EtablissemtForm(forms.ModelForm):
    
    class Meta:
        model = Etablissements
        fields = ('image','designationEcole','arreteMin','adresse','telephone','email','typesEcole','degree','biographie')
 
 

class TestForm(models.ModelForm):
    class Meta:
        model = Test
        fields = ('typesEcole', 'degree')