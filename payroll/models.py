from django.db import models

class Employee(models.Model):
    """Modelo que representa los datos de empleados filtrados por permisos.""" 
    EmployeeID = models.AutoField(primary_key=True)  # Coincide con EmployeeID
    FirstName = models.CharField(max_length=50)      # Coincide con FirstName
    LastName = models.CharField(max_length=50)       # Coincide con LastName
    DepartmentID = models.IntegerField()             # Coincide con DepartmentID
    Salary = models.DecimalField(max_digits=10, decimal_places=2)  # Coincide con Salary

    class Meta:
        managed = False
        db_table = 'vw_EmployeeData' 