from django.contrib import admin
from .models import Grupo
from .models import Area
from .models import Programa
from .models import Peso
from .models import Pais
from .models import Universidad
from .models import ProgramaU
from .models import PesoU

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numeral','nombre',)

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'grupo', 'numeral','nombre', )

class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)

class PesoAdmin(admin.ModelAdmin):
    list_display = ('id', 'area', 'min', 'max', 'programa', ) 
    
class UniversidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'pais',)
    
class ProgramaUAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'universidad',)

class PesoUAdmin(admin.ModelAdmin):
    list_display = ('id', 'area','min','max','programau',)

class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', )

admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Programa, ProgramaAdmin)
admin.site.register(Peso, PesoAdmin)
admin.site.register(Universidad, UniversidadAdmin)
admin.site.register(ProgramaU, ProgramaUAdmin)
admin.site.register(PesoU, PesoUAdmin)
admin.site.register(Pais, PaisAdmin)


