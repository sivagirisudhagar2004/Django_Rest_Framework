from django.urls import path,include
from .views import *

urlpatterns = [

    path('task/',TaskView.as_view()),
    path('task/<int:task_id>/',TaskView.as_view()),
    
]