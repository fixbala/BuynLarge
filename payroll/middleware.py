import pyodbc
from django.db import connections

class SQLServerUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            username = request.user.username
            # Cambiar el usuario de la conexión a SQL Server
            with connections['default'].cursor() as cursor:
                cursor.execute(f"SETUSER '{username}'")
        response = self.get_response(request)
        return response 