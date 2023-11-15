from rest_framework import serializers
from .models import *

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
        
class EmpleadoSerializer(serializers.ModelSerializer):

    departamento_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Empleado
        fields = '__all__'

    def get_departamento_nombre(self, obj):
        return obj.departamento.nombre
        
class EquipoSerializer(serializers.ModelSerializer):

    empleado_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Equipo
        fields = '__all__'

    def get_empleado_nombre(self, obj):
        return obj.usuario.nombre
        
class TelefonoSerializer(serializers.ModelSerializer):

    empleado_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Telefono
        fields = '__all__'

    def get_empleado_nombre(self, obj):
        return obj.usuario.nombre

class ImpresoraSerializer(serializers.ModelSerializer):

    departamento_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Impresora
        fields = '__all__'

    def get_departamento_nombre(self, obj):
        return obj.departamento.nombre
        
class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = '__all__'
        
class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = '__all__'
        
class DesincorporacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Desincorporacion
        fields = '__all__'

class SolvenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solvencia
        fields = '__all__'