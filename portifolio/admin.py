from django.contrib import admin

from .models import Formulario, Projetos, ProjetosTags, ProjetosFuncionalidades, Tags, Funcionalidades

# Register your models here.
admin.site.register(Formulario)
admin.site.register(Projetos)
admin.site.register(Tags)
admin.site.register(Funcionalidades)
admin.site.register(ProjetosTags)
admin.site.register(ProjetosFuncionalidades)

