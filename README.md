# inventorySystem
Un sistema para manejar inventario de activos 

Requisitos: Instalar Python 3.12, Instalar Postgre (ultima version)

Paso 1: Descargar archivos de proyecto

Paso 2: Crear un entorno virtual de Python
	`python -m venv "nombredelentorno"`

Paso 2.1: Crear una carpeta llamada "Proyecto"

Paso 2.2: Arrastrar "manage.py" y las carpetas "database" e "inventario" dentro de la nueva carpeta creada

Paso 2.3: Arrastrar la carpeta "Proyecto" dentro de la carpeta del entorno virtual creado

Paso 2.4: Abrir Powershell como administrador y modificar las politicas de ejecucion con el comando	
	`Set-ExecutionPolicy Unrestricted`

Paso 2.5: Activar el entorno virtual, puede ser realizado con uno de los siguientes metodos
	En Visual Studio Code arrastrar el archivo activate.ps1 al terminal de VSC
	En CMD escribir "activate" en el directorio que contenga 

Paso 3: Descargar los requerimientos del entorno virtual
	`pip install -r requirements.txt`

Paso 4: Crear una base de datos en Postgre que lleva por nombre inventario 

Paso 5: Migrar a la base dde datos
	`python manage.py makemigrations`
 	En caso de dar error con algunas tablas usar:
	`python manage.py makemigrations --merge`
 	Continuar con:
	`python manage.py migrate`

Paso 6: Crear super usuario (el administrador del proyecto)
	`python manage.py createsuperuser`

Paso 7: Correr el servidor
	`python manage.py runserver 8000`
