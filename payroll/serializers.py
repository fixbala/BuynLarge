from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """Serializador para los datos de empleados.""" 
    class Meta:
        model = Employee
        fields = '__all__' 