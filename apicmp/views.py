from django.shortcuts import render

from rest_framework import viewsets
from .models import Grupo
from .models import Area
from .models import Programa
from .models import Peso
from .models import PesoU
from .models import ProgramaU
from .models import Universidad

from .serializers import GrupoSerializer
from .serializers import AreaSerializer
from .serializers import ProgramaSerializer
from .serializers import PesoSerializer
from .serializers import ProgramaUSerializer
from .serializers import PesoUSerializer
from .serializers import UniversidadSerializer

class GrupoView(viewsets.ReadOnlyModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    #permission_classes = [permissions.IsAuthenticated,]

class AreaView(viewsets.ReadOnlyModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class ProgramaView(viewsets.ReadOnlyModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

class PesoView(viewsets.ReadOnlyModelViewSet):
    queryset = Peso.objects.all()
    serializer_class = PesoSerializer

class ProgramaUView(viewsets.ReadOnlyModelViewSet):
    queryset = ProgramaU.objects.all()
    serializer_class = ProgramaUSerializer

class PesoUView(viewsets.ReadOnlyModelViewSet):
    queryset = PesoU.objects.all()
    serializer_class = PesoUSerializer  

class UniversidadView(viewsets.ReadOnlyModelViewSet):
    queryset = Universidad.objects.all()
    serializer_class = UniversidadSerializer  