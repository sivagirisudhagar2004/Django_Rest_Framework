from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import Task_Serializers

class TaskView(APIView):

    def post(self,request):

        new_task = Task_Serializers(data = request.data)

        if(new_task.is_valid()):
            new_task.save()
            return Response("New Task Added")
        else:
            return Response(new_task.errors)

