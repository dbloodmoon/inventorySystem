from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all().order_by('id')
    serializer_class = DepartamentoSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        return queryset

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        return queryset
    
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        return queryset
    
class TelefonoViewSet(viewsets.ModelViewSet):
    queryset = Telefono.objects.all()
    serializer_class = TelefonoSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        return queryset
    
class ImpresoraViewSet(viewsets.ModelViewSet):
    queryset = Impresora.objects.all()
    serializer_class = ImpresoraSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        return queryset
    
class SwitchViewSet(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        return queryset
    
class RouterViewSet(viewsets.ModelViewSet):
    queryset = Router.objects.all()
    serializer_class = RouterSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        return queryset

class DesincorporacionViewSet(viewsets.ModelViewSet):
    queryset = Desincorporacion.objects.all()
    serializer_class = DesincorporacionSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        usuario_nombre = self.request.query_params.get('usuario', None)
        if usuario_nombre is not None:
            queryset = queryset.filter(name=usuario_nombre)
        return queryset
    
class SolvenciaViewset(viewsets.ModelViewSet):
    queryset = Solvencia.objects.all()
    serializer_class = SolvenciaSerializer