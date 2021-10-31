from django.db import models

# Create your models here.

class Departaments(models.Model):
    DepartamentId = models.AutoField(primary_key=True)
    DepartamentName = models.CharField(max_length=100)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Departament = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)

