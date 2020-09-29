from rest_framework import serializers
from .models import Grupo
from .models import Area
from .models import Programa
from .models import Peso
from .models import PesoU
from .models import ProgramaU
from .models import Universidad

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

class UniversidadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Universidad
    fields = '__all__'
  

class PesoUSerializer(serializers.ModelSerializer):

  class Meta:
    model = PesoU
    fields = ['id', 'min', 'max', 'area']  

class ProgramaUSerializer(serializers.ModelSerializer): 
  pesosu =  PesoUSerializer(many=True, read_only=True)
  class Meta:
    model = ProgramaU
    fields = ['id', 'nombre', 'universidad', 'pesosu']
