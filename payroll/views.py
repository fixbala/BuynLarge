from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """Vista que expone datos de empleados con permisos aplicados en SQL Server.""" 
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 
 