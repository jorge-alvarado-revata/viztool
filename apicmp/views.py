from django.shortcuts import render

from rest_framework import viewsets
from .models import Grupo
from .models import Area
from .models import Programa
from .models import Peso
from .serializers import GrupoSerializer
from .serializers import AreaSerializer
from .serializers import ProgramaSerializer
from .serializers import PesoSerializer

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
