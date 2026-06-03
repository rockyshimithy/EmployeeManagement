from rest_framework import serializers
from .models import Employee, Feira


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')

class FeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feira
        fields = ('url',
                  'id',
                  'longi',
                  'lat',
                  'setcens',
                  'areap',
                  'coddist',
                  'distrito',
                  'codsubpref',
                  'subprefe',
                  'regiao5',
                  'regiao8',
                  'nome_feira',
                  'registro',
                  'logradouro',
                  'numero',
                  'bairro',
                  'referencia')

