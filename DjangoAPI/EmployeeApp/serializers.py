from rest_framework import serializers
from EmployeeApp.models import Departaments, Employees

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departaments 
        fields = ('DepartamentId',
                'DepartamentName')
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees 
        fields = ('EmployeeId',
                'EmployeeName',
                'Departament',
                'DateOfJoining',
                'PhotoFileName')
    