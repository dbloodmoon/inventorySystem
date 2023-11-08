from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin

# Departamentos

class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('nombre',)
    
    # Campos visibles en admin
    list_display = ('nombre',)

admin.site.register(Departamento, DepartamentoAdmin)

# Computadores y Laptops

class EmpleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('nombre', 'cedula')
    
    # Campos visibles en admin
    list_display = ('nombre', 'departamento', 'cargo', 'cedula')
    
    # Campos filtrables en admin
    list_filter = ('departamento', 'cargo')

admin.site.register(Empleado, EmpleadoAdmin)

class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('usuario__nombre',)
    
    # Campos visibles en admin
    list_display = ('usuario', 'procesador', 'ram', 'almacenamiento', 'tipo_disco', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('usuario__departamento', 'usuario__cargo')

admin.site.register(Equipo, EquipoAdmin)

class ImpresoraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('marca', 'modelo')
    
    # Campos visibles en admin
    list_display = ('marca', 'modelo', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('marca',)

admin.site.register(Impresora, ImpresoraAdmin)

class TelefonoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('usuario__nombre', 'numero')
    
    # Campos visibles en admin
    list_display = ('usuario', 'numero', 'marca', 'modelo', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('usuario__departamento', 'usuario__cargo',)

admin.site.register(Telefono, TelefonoAdmin)

class SwitchAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('marca', 'modelo')
    
    # Campos visibles en admin
    list_display = ('marca', 'modelo', 'puertos', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('marca',)

admin.site.register(Switch, SwitchAdmin)

class RouterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('marca', 'modelo')
    
    # Campos visibles en admin
    list_display = ('marca', 'modelo', 'puertos', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('marca',)

admin.site.register(Router, RouterAdmin)

class DesincorporacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('marca', 'modelo')
    
    # Campos filtrables en admin
    list_filter = ('departamento',)
    
admin.site.register(Desincorporacion, DesincorporacionAdmin)