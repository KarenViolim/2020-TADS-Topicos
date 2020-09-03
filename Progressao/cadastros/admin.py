from django.contrib import admin

from .models import Marca, Grupo, Equipamento, Cliente, Funcionario

# Register your models here.
admin.site.register(Marca)
admin.site.register(Grupo)
admin.site.register(Equipamento)
admin.site.register(Cliente)
admin.site.register(Funcionario)
