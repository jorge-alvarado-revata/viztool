from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'grupo', views.GrupoView, basename='Grupo')
router.register(r'area', views.AreaView, basename='Area')
router.register(r'programa', views.ProgramaView, basename='Programa')
router.register(r'peso', views.PesoView, basename='Peso')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]