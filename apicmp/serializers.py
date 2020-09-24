from rest_framework import serializers
from .models import Grupo
from .models import Area
from .models import Programa
from .models import Peso

class AreaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Area
    fields = ['id','numeral', 'nombre']

class GrupoSerializer(serializers.ModelSerializer):
  areas = AreaSerializer(many=True, read_only=True)
  class Meta:
    model = Grupo
    fields = ['id','numeral','nombre','areas']



class PesoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Peso
    fields = ['id', 'min', 'max', 'area']  

class ProgramaSerializer(serializers.ModelSerializer): 
  pesos =  PesoSerializer(many=True, read_only=True)
  class Meta:
    model = Programa
    fields = ['id', 'nombre', 'pesos']


