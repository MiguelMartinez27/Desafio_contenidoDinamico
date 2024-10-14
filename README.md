# Desafio Mostrando Contenido Dinamico
Este repositorio consiste en demostrar cómo mostrar una lista de empleados de manera dinámica en una página web utilizando Django., correspondiente al modulo 6 "Introduccion a
Django" para el bootcamp full stack python de talento digital.

## Descripcion
El objetivo es desarrollar una aplicación en Django que despliegue una lista de nombres de empleados, almacenada en una lista de Python, cuya cantidad es variable.
Esta lista se visualizará en una plantilla HTML.

## Requerimientos
- SO windows, Mac OS o Linux
- Python 3.12 o superior
- Entorno virtual
- Django 5.1

## Instalacion
Clonar este repositorio:

```
git clone https://github.com/MiguelMartinez27/Desafio_contenidoDinamico.git
cd Desafio_contenidoDjango
```
Crear y activar el entorno virtual:
```
python -m venv venv
source myenv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```
Instalar las dependencias:
```
pip install django
```

Ejecutar las migraciones:
```
python manage.py migrate
```
Iniciar el servidor de desarrollo:
```
python manage.py runserver
```
Acceder a la URL:
En tu navegador ingresa a ```127.0.0.1:8000/empleados/vista/``` para ver la lista de empleados.


## Autor
Miguel Martinez F.
