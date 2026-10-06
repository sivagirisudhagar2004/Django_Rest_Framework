from django.urls import path,include
from .views import *

urlpatterns = [
    path('details/',StudentAPI.as_view()),
    path('details/<int:id>/',StudentAPI.as_view()),

    path('task/',TaskView.as_view())
]