from django.urls import path
from .views import *

urlpatterns = [

    path('add_emp/', add_employee),

    path('get_emp/', get_employee),

    path('get_emp_by_id/<int:id>/', get_employee_by_id),

    path('delete_emp/<int:id>/', delete_employee),
]