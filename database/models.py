from django.db import models

# Modelo de departamentos, rige el modelo de empleados

class Departamento(models.Model):

    nombre = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.nombre

# Modelo de empleados, determina la responsabilidad de los equipos

CARGOS = [('Gerente', 'Gerente'), 
          ('Jefe', 'Jefe'),
          ('Coordinador', 'Coordinador'),
          ('Especialista', 'Especialista'),
          ('Supervisor', 'Supervisor'),
          ('Diseñador', 'Diseñador'),
          ('Programador', 'Programador'), 
          ('Soporte', 'Soporte'),
          ('Analista', 'Analista'),]

class Empleado(models.Model):   
    
    nombre = models.CharField(max_length=50, default='')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cargo = models.CharField(choices=CARGOS, max_length=50, default='')
    cedula = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.cedula)

# Computadores y Laptops

class Equipo(models.Model):   
    
    # Datos corporativos
    
    usuario = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    bien_nacional = models.CharField(max_length=6, default="")
    # Datos de fabrica

    marca = models.CharField(max_length=50, default='')
    modelo = models.CharField(max_length=50, default='')
    
    procesador = models.CharField(max_length=50, default='')
    ram = models.IntegerField(default=0)
    almacenamiento = models.IntegerField(default=0)
    tipo_disco = models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], max_length=50, default='')
    
    # Datos de Red
    
    ipv4 = models.CharField(max_length=50, default='')
    mac = models.CharField(max_length=50, default='')

    def __str__(self):
        return str(self.usuario.cedula)
# Telefonos celulares    

class Telefono(models.Model):   
    
    # Datos corporativos
    
    usuario = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    numero = models.CharField(max_length=50, default='')
    bien_nacional = models.CharField(max_length=6, default="")

    # Datos de fabrica

    marca = models.CharField(max_length=50, default='')
    modelo = models.CharField(max_length=50, default='')
    
    # Datos de Red
    
    ipv4 = models.CharField(max_length=50, default='')
    mac = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.usuario.nombre
    
class Impresora(models.Model):

    # Datos corporativos
    
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    bien_nacional = models.CharField(max_length=6, default="")

    # Datos de fabrica
    
    marca = models.CharField(max_length=50, default='')
    modelo = models.CharField(max_length=50, default='')
    
    # Datos de red 
    
    ipv4 = models.CharField(max_length=50, default='')
    mac = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.ipv4 + ' ' + self.departamento.nombre
    
    
class Switch(models.Model):

    # Datos corporativos
    
    bien_nacional = models.CharField(max_length=6, default="")

    # Datos de fabrica

    marca = models.CharField(max_length=50, default='')
    modelo = models.CharField(max_length=50, default='')
    puertos = models.IntegerField(default=0)
    
    # Datos de Red
    
    ipv4 = models.CharField(max_length=50, default='')
    mac = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.ipv4

class Router(models.Model):
    
    # Datos corporativos
    
    bien_nacional = models.CharField(max_length=6, default="")
    
    # Datos de fabrica

    marca = models.CharField(max_length=50, default='')
    modelo = models.CharField(max_length=50, default='')
    puertos = models.IntegerField(default=0)
    
    # Datos de Red
    
    ipv4 = models.CharField(max_length=50, default='')
    mac = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.ipv4
    
class Desincorporacion(models.Model):
    
    # Datos de usuario
    
    bien_nacional = models.CharField(max_length=6, default="")
    
    # Datos corporativos

    descripcion = models.CharField(max_length=100, default='')
    
    # Datos de fabrica

    responsable = models.ForeignKey(Equipo, on_delete=models.CASCADE, default=0)
    marca = models.CharField(max_length=50, default='')
    modelo = models.CharField(max_length=50, default='')
    
    def __str__(self):
        return str(self.responsable.usuario.cedula) + " " + self.modelo
