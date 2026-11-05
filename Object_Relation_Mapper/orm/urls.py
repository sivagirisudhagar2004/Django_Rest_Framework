from django.urls import path,include
from .views import *

urlpatterns =[
    path('api/',StudentView.as_view())
]