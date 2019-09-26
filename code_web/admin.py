from django.contrib import admin
from code_web.models import *

class admin_usuarios(admin.ModelAdmin):
    list_display = ("nombre","email","comentarios")
    search_fields = ["nombre","email"]
    
admin.site.register(usuarios_registrados,admin_usuarios)