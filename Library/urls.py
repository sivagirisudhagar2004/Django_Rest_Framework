from django.urls import path,include
from .router import library_router
from .views import *

urlpatterns = [
    path('api/',include(library_router)),
    path('laptop/',LaptopView.as_view()),
    path('laptop/<int:pk>/',LaptopViewById.as_view())
]