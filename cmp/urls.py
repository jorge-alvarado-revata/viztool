from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Viz Tool'
admin.site.index_title = 'Herramienta para visualizar datos programas'
admin.site.site_title = 'Viz Tool' 

urlpatterns = [
    path('apicmp/', include('apicmp.urls')),
    path('admin/', admin.site.urls),
]
