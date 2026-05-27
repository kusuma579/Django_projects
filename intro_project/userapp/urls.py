
from django.urls import path

from .views import great,get_name,user_data,greet_to_user

urlpatterns = [
    path("message", great),
    path("name",get_name),
    path("data",user_data),
    path ("user_message/<str:name>/<int:age>",greet_to_user)
]