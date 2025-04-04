# Sistema de Control de Permisos - BuyNLarge

Sistema de permisos granular para una API de nómina, desarrollado para Buy n Large como parte de una prueba técnica. Permite restringir el acceso a tablas y registros según el rol del usuario, con la lógica de permisos implementada en SQL Server y expuesta a través de una API con Django Rest Framework.

## Creación y Desarrollo

### Tecnologías Utilizadas
- **Python 3.13.2**: Lenguaje principal.
- **Django 5.0**: Framework web.
- **Django Rest Framework 3.16.0**: Para crear la API.
- **mssql-django**: Adaptador para conectar Django con SQL Server.
- **SQL Server (Developer Edition)**: Base de datos con lógica de permisos.
- **ODBC Driver 17 for SQL Server**: Driver para la conexión.
- **Visual Studio Code**: Entorno de desarrollo en Windows.

### Proceso de Desarrollo
1. **Configuración del Entorno**:
   - Instalación de Python, SQL Server, y VS Code.
   - Creación de un entorno virtual: `python -m venv venv`.
   - Instalación de dependencias: `pip install django==5.0 djangorestframework==3.16.0 mssql-django pyodbc`.

2. **Estructura del Proyecto**:
   - Proyecto Django: `django-admin startproject buynlarge`.
   - Aplicación: `python manage.py startapp payroll`.
   - Configuración en `settings.py` para SQL Server y DRF.

3. **Base de Datos**:
   - Creación de la base `BuyNLargeDB` en SQL Server.
   - Diseño en tercera forma normal con tablas: `Roles`, `Users`, `Departments`, `Employees`, `Permissions`.
   - Vista `vw_EmployeeData` para aplicar permisos granulares.

4. **API**:
   - Modelo en `payroll/models.py` mapeado a la vista.
   - Serializador y vista en `payroll/serializers.py` y `payroll/views.py`.
   - Rutas en `payroll/urls.py` y `buynlarge/urls.py`.

5. **Autenticación**:
   - Integración de `TokenAuthentication` de DRF.
   - Middleware en `payroll/middleware.py` para pasar el usuario autenticado a SQL Server.

## Configuraciones

### `settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'BuyNLargeDB',
        'USER': 'sa',
        'PASSWORD': '<tu_contraseña>',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server'},
    }
}

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'payroll',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
}

MIDDLEWARE = [
    ...
    'payroll.middleware.SQLServerUserMiddleware',
] 

Estructura de Archivos

buynlarge/
├── buynlarge/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── payroll/
│   ├── middleware.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── README.md
└── requirements.txt

Requisitos para Usarla:
Instalar Dependencias:
>>pip install -r requirements.txt
Configurar SQL Server:
Crea la base BuyNLargeDB.
Ejecuta las consultas SQL del archivo sql_queries.sql.
Migraciones:
>>python manage.py migrate
Crear Usuarios y Tokens:
>>python manage.py shell
>>>from django.contrib.auth.models import User
>>>from rest_framework.authtoken.models import Token
>>>User.objects.create_user('admin_user', password='password123')
>>>User.objects.create_user('hr_user', password='password123')
>>>User.objects.create_user('emp_user', password='password123')
>>>for user in User.objects.all(): Token.objects.get_or_create(user=user)

Uso:
Iniciar el Servidor: 
>>python manage.py runserver
Acceder al Endpoint:
curl -H "Authorization: Token <token>" http://127.0.0.1:8000/api/employees/
