from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
import json

@csrf_exempt
def add_employee(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if Employee.objects.filter(email=data['email']).exists():
                return JsonResponse({
                    "status": "failed",
                    "message": "Email already exists"
                })
            employee = Employee.objects.create(
                name=data['name'],
                email=data['email'],
                salary=data['salary'],
                profession=data['profession'],
                designation=data['designation'],
                phone=data['phone']
            )
            return JsonResponse({
                "status": "success",
                "message": "Employee added successfully",
                "employee_id": employee.id
            })
        except KeyError as e:
            return JsonResponse({
                "status": "failed",
                "message": f"Missing field: {str(e)}"
            })
        except Exception as e:
            return JsonResponse({
                "status": "failed",
                "message": str(e)
            })
    return JsonResponse({
        "status": "failed",
        "message": "Only POST method allowed"
    })

@csrf_exempt
def get_employee(request):
    if request.method == "GET":
        try:
            employees = Employee.objects.all().values()
            return JsonResponse({
                "status": "success",
                "data": list(employees)
            })
        except Exception as e:
            return JsonResponse({
                "status": "failed",
                "message": str(e)
            })
    return JsonResponse({
        "status": "failed",
        "message": "Only GET method allowed"
    })
@csrf_exempt
def get_employee_by_id(request, id):
    if request.method == "GET":
        try:
            employee = Employee.objects.get(id=id)
            data = {
                "id": employee.id,
                "name": employee.name,
                "email": employee.email,
                "salary": employee.salary,
                "profession": employee.profession,
                "designation": employee.designation,
                "phone": employee.phone
            }
            return JsonResponse({
                "status": "success",
                "data": data
            })
        except Employee.DoesNotExist:
            return JsonResponse({
                "status": "failed",
                "message": "Employee not found"
            })
        except Exception as e:
            return JsonResponse({
                "status": "failed",
                "message": str(e)
            })
    return JsonResponse({
        "status": "failed",
        "message": "Only GET method allowed"
    })
@csrf_exempt
def delete_employee(request, id):
    if request.method == "DELETE":
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
            return JsonResponse({
                "status": "success",
                "message": "Employee deleted successfully"
            })
        except Employee.DoesNotExist:
            return JsonResponse({
                "status": "failed",
                "message": "Employee not found"
            })
        except Exception as e:
            return JsonResponse({
                "status": "failed",
                "message": str(e)
            })
    return JsonResponse({
        "status": "failed",
        "message": "Only DELETE method allowed"
    })