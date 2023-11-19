from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from . models import *
from import_export.admin import ImportExportModelAdmin
from django.apps import apps
from django.db.models import ForeignKey

# Departamentos

def busqueda_empleado(modeladmin, request, queryset):
   results = []
   for obj in queryset:
       for model in apps.get_models():
           for field in model._meta.get_fields():
               if isinstance(field, ForeignKey) and field.related_model == Empleado:
                  related_objects = model.objects.filter(**{f'{field.name}': obj})
                  for related_obj in related_objects:
                      results.append(related_obj)
   print(results)

   # Crear PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
   c = canvas.Canvas(response)

   # Generacion de texto segun campos
   for item in results:
       y_position = 750
       for field_name in item._meta.get_fields():
           field_value = getattr(item, field_name.name)
           c.drawString(100, y_position, f"{field_name.name.capitalize()}: {field_value}")
           y_position -= 20

       c.showPage()

   c.save()
   return response

busqueda_empleado.short_description = "Buscar por Empleado"

class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    # Campos buscables en admin
    search_fields = ('nombre',)
    
    # Campos visibles en admin
    list_display = ('nombre',)

admin.site.register(Departamento, DepartamentoAdmin)

# Computadores y Laptops

class EmpleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
   actions = [busqueda_empleado]    

   # Campos buscables en admin
   search_fields = ('nombre', 'cedula')

   # Campos visibles en admin
   list_display = ('nombre', 'departamento', 'cargo', 'cedula')

   # Campos filtrables en admin
   list_filter = ('departamento', 'cargo')

admin.site.register(Empleado, EmpleadoAdmin)
def equipo_no_operativo(modeladmin, request, queryset):
    for obj in queryset:
        # Create a new SourceModel object with the same dat
        
        if (hasattr(obj, 'usuario')):
            
            source_obj = NoFuncional.objects.create(
            bien_nacional=obj.bien_nacional,
            usuario=obj.usuario,
            marca=obj.marca,
            modelo=obj.modelo
            )
        else:   
            
            source_obj = NoFuncional.objects.create(
            bien_nacional=obj.bien_nacional,
            usuario= None,
            marca=obj.marca,
            modelo=obj.modelo
            )
            
        # Delete the TargetModel object
        obj.delete()

equipo_no_operativo.short_description = "Marcar como activo no operativo"

def equipo_en_solvencia(modeladmin, request, queryset):
        
    for obj in queryset:
        
        if (hasattr(obj, 'usuario')):
            
            source_obj = Solvencia.objects.create(
            tipo = obj.__class__.__name__,
            bien_nacional=obj.bien_nacional,
            marca=obj.marca,
            usuario= None,
            modelo=obj.modelo
            )
            
        elif(hasattr(obj, 'departamento')):
            source_obj = Solvencia.objects.create(
            tipo = obj.__class__.__name__,
            bien_nacional=obj.bien_nacional,
            marca=obj.marca,
            departamento=obj.departamento,
            modelo=obj.modelo
            )
            
        else:   
            
            source_obj = Solvencia.objects.create(
            tipo = obj.__class__.__name__,
            bien_nacional=obj.bien_nacional,
            marca=obj.marca,
            modelo=obj.modelo
            )
            
        obj.delete()

equipo_en_solvencia.short_description = "Marcar como activo en solvencia"


def reasignar_equipo(modeladmin, request, queryset):
   for obj in queryset:
       target = obj.tipo
       target_model = apps.get_model('database', target)

       if (hasattr(obj, 'usuario')):
           source_obj = target_model.objects.create(
               bien_nacional=obj.bien_nacional,
               marca=obj.marca,
               modelo=obj.modelo
           )
           
       elif(hasattr(obj, 'departamento')):
           source_obj = target_model.objects.create(
               bien_nacional=obj.bien_nacional,
               departamento=obj.departamento,
               marca=obj.marca,
               modelo=obj.modelo
           )
       else:  
           source_obj = Solvencia.objects.create(
               bien_nacional=obj.bien_nacional,
               usuario= None,
               marca=obj.marca,
               modelo=obj.modelo
           )
           
       obj.delete()

reasignar_equipo.short_description = "Reasignar equipo"

def generar_pdf(modeladmin, request, queryset):
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

   p = canvas.Canvas(response)
   
#  Obtiene el modelo 
   model = modeladmin.model
   model_name = model._meta.verbose_name_plural.capitalize()
#  Obtiene los campos
   fields = [field.name for field in model._meta.fields]

   for item in queryset:
        # Dibuja el encabezado
        y_position = 750
        for field_name in fields:
            field_value = getattr(item, field_name)
            p.drawString(100, y_position, f"{field_name.capitalize()}: {field_value}")
            y_position -= 20

        p.showPage()

   p.save()
   return response

generar_pdf.short_description = "Generar PDF"

class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia, generar_pdf]

    # Campos buscables en admin
    search_fields = ('usuario__nombre', 'bien_nacional')
    
    # Campos visibles en admin
    list_display = ('usuario', 'bien_nacional', 'procesador', 'ram', 'almacenamiento', 'tipo_disco', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('usuario__departamento', 'usuario__cargo', 'usuario__nombre')

admin.site.register(Equipo, EquipoAdmin)

class ImpresoraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia, generar_pdf]

    # Campos buscables en admin
    search_fields = ('marca', 'modelo', 'bien_nacional')
    
    # Campos visibles en admin
    list_display = ('marca', 'bien_nacional', 'modelo', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('marca', 'departamento__nombre')

admin.site.register(Impresora, ImpresoraAdmin)

class TelefonoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia, generar_pdf]

    # Campos buscables en admin
    search_fields = ('usuario__nombre', 'numero', 'bien_nacional')
    
    # Campos visibles en admin
    list_display = ('usuario', 'bien_nacional', 'numero', 'marca', 'modelo', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('usuario__departamento', 'usuario__cargo',)

admin.site.register(Telefono, TelefonoAdmin)

class SwitchAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia, generar_pdf]

    # Campos buscables en admin
    search_fields = ('marca', 'modelo', 'bien_nacional')
    
    # Campos visibles en admin
    list_display = ('bien_nacional', 'marca', 'modelo', 'puertos', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('marca',)

admin.site.register(Switch, SwitchAdmin)

class RouterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia, generar_pdf]
    
    # Campos buscables en admin
    search_fields = ('marca', 'modelo', 'bien_nacional')
    
    # Campos visibles en admin
    list_display = ('bien_nacional', 'marca', 'modelo', 'puertos', 'ipv4', 'mac')
    
    # Campos filtrables en admin
    list_filter = ('marca',)

admin.site.register(Router, RouterAdmin)


class PerifericosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    actions = [equipo_no_operativo, equipo_en_solvencia, generar_pdf]

    # Campos visibles en admin
    list_display = ('bien_nacional', 'usuario', 'marca', 'modelo')
    
    # Campos buscables en admin
    
    search_fields = ('bien_nacional', 'marca', 'modelo')
    # Campos filtrables en admin
    
admin.site.register(Periferico, PerifericosAdmin)

class DesincorporacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    # No se permite la creacion de objetos
    def has_add_permission(self, request):
       return False

    actions = [generar_pdf]

    # Campos visibles en admin
    list_display = ('bien_nacional', 'usuario', 'marca', 'modelo')
    
    # Campos buscables en admin
    
    search_fields = ('bien_nacional', 'marca', 'modelo')
    # Campos filtrables en admin
    
admin.site.register(NoFuncional, DesincorporacionAdmin)

class SolvenciaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
     
    # No se permite la creacion de objetos
    def has_add_permission(self, request):
       return False

    actions = [generar_pdf, reasignar_equipo]

    # Campos visibles en admin
    list_display = ('bien_nacional', 'tipo', 'usuario', 'marca', 'modelo')
    
    # Campos buscables en admin
    
    search_fields = ('bien_nacional', 'marca', 'modelo')
    # Campos filtrables en admin
    
    
admin.site.register(Solvencia, SolvenciaAdmin)

