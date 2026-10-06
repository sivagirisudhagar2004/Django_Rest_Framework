from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import Task_Serializers

class TaskView(APIView):

    def get(self,request,task_id=None):

        if(task_id == None):

         all_task = Task.objects.all()

         task_data = Task_Serializers(all_task, many=True).data

         return Response(task_data)
        
        else:
            task = Task.objects.get(id = task_id)

            task_data = Task_Serializers(task).data

            return Response(task_data)

    def post(self,request):

        new_task = Task_Serializers(data = request.data)

        if(new_task.is_valid()):
            new_task.save()
            return Response("New Task Added")
        else:
            return Response(new_task.errors)
    
    def patch(self,request,task_id):

        task = Task.objects.get(id = task_id)

        update_task = Task_Serializers(task,data = request.data, partial = True)

        if(update_task.is_valid()):

            update_task.save()

            return Response("Task Updated")
        else:
            return Response(update_task.errors)

    def put(self,request,task_id):

        task = Task.objects.get(id = task_id)

        update_task = Task_Serializers(task,data = request.data, partial = True)

        if(update_task.is_valid()):

            update_task.save()
            
            return Response("Task Updated")
        else:
            return Response(update_task.errors)

    def delete(self, request,task_id):

        task = Task.objects.get(id = task_id)

        task.delete()

        return Response("Task Deleted")