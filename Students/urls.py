from django.urls import path,include
from .views import *

urlpatterns = [

    path('details/',StudentAPI.as_view()),
    path('details/<int:student_id>/',StudentAPI.as_view()),


    path('task/',TaskView.as_view()),
    path('task/<int:task_id>/',TaskView.as_view()),

    path('mark/',RanksheetView.as_view()),
    path('mark/<int:id>/',RanksheetView.as_view()),

    path('tast/list/create',task_list_create),
    path('tast/update/delete/<int:id>/',task_update_delete)
    
]