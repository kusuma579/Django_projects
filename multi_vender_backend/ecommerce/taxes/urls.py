from django.urls import path

from .views import (
    CreateTaxView,
    GenerateBillView
)

urlpatterns = [

    path(
        'create/',
        CreateTaxView.as_view(),
        name='create-tax'
    ),

    path(
        'bill/<int:order_id>/',
        GenerateBillView.as_view(),
        name='generate-bill'
    ),
]