from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def great(request):
    return HttpResponse('Hii, Good Morning')

def get_name(request):
    return HttpResponse('My name is Sravya')

def user_data(request):
    return HttpResponse([
        {
            'name':'Sravya',
            "email":"sravya@gmail.com",
            "age":18
        },
        {
            "name":"rajasri",
            "email":"rajasri@gmail.com",
            "age":19
        },
        {
            "name":"monika",
            "email":"monika@gmail.com",
            "age":20
        }
    ])
def greet_to_user(request,name,age):
    return HttpResponse(f'Hii, {name} Good Morning your age is {age}')