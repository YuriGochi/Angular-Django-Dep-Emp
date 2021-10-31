from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Departaments,Employees
from EmployeeApp.serializers import DepartamentSerializer, EmployeeSerializer
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def departamentApi(request,id=0):
    if request.method=='GET':
        departaments = Departaments.objects.all()
        departaments_serializer = DepartamentSerializer(departaments, many=True)
        return JsonResponse(departaments_serializer.data, safe=False)
    elif request.method=='POST':
        departament_data=JSONParser().parse(request)
        departament_serializer = DepartamentSerializer(data=departament_data)
        if departament_serializer.is_valid():
            departament_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        departament_data = JSONParser().parse(request)
        departament=Departaments.objects.get(DepartamentId=departament_data['DepartamentId'])
        departament_serializer=DepartamentSerializer(departament, data=departament_data)
        if departament_serializer.is_valid():
            departament_serializer.save()
            return JsonResponse("Update Successfuly", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method=='DELETE':
        departament=Departaments.objects.get(DepartamentId=id)
        departament.delete()
        return JsonResponse("Deleted Successfuly", safe=False)

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee= Employees.objects.get(EmployeeId = employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee, data = employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Update Successfuly", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfuly", safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)