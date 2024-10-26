from rest_framework import serializers
from .models import *

class EtablissementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Etablissements
        fields = ('image', 'designationEcole', 'arreteMin', 'adresse', 'telephone', 'email', 'typesEcole', 'degree', 'biographie')


class TestSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('typesEcole', 'degree')