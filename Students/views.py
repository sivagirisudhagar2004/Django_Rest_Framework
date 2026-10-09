from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from  rest_framework.decorators import api_view
from decouple import config
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class StudentAPI(APIView):

    permission_classes = [IsAuthenticated]
    def get(self,request):
        all_students = Student.objects.all()
        student_data = Student_Task_Serializer(all_students,many=True).data
        #student_list = []
        #for s in all_students:
         #   student_dict = {
          #      'id':s.id,
           #     'name':s.name,
           #     'age':s.age
            #}
            #student_list.append(student_dict)

        return Response(student_data) #student_list

    def post(self,request):

        new_student = Student(name = request.data['name'],age = request.data['age'])
        new_student.save()
    
        return Response("New Student Created")

    def put(self,request,student_id):

        student_data = Student.objects.filter(id = student_id)

        student_data.update(name = request.data['name'],age = request.data['age'])

        return Response("Student Data Updated")

    def patch(self,request,student_id):

        student_data = Student.objects.filter(id = student_id)

        student_data.update(name = request.data['name'],age = request.data['age'])

        return Response("Student Data Updated")

    def delete(self,request,student_id):

        student_data = Student.objects.get(id = student_id)
        
        student_data.delete()

        return Response("Student Data Deleted")

class TaskView(APIView):

    def get(self,request,task_id=None):

        if(task_id == None):

         all_task = Task.objects.all()

         task_data = Task_Data_Serilizes(all_task, many=True).data #task_serilizer

         return Response(task_data)
        
        else:
            task = Task.objects.get(id = task_id)

            task_data = Task_Data_Serilizes(task).data

            return Response(task_data)

    def post(self,request):

        new_task = Task(student_reference_id = request.data['student_reference'],task_name = request.data['task_name'],description = request.data['description'])

        new_task.save()

        return Response("Task Created")

        #new_task = Task_Serializers(data = request.data)

        #if(new_task.is_valid()):
         #   new_task.save()
          #  return Response("New Task Added")
        #else:
         #   return Response(new_task.errors)
    
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

class RanksheetView(APIView):

    def get(self,request,id = None):

        if (id == None):

            all_rank = RankSheet.objects.all()

            rank_data = RankSheet_Serilizes(all_rank, many = True).data

            return Response(rank_data)
        else:
            rank = RankSheet.objects.get( id = id)

            rank_data = RankSheet_Serilizes(rank).data

            return Response(rank_data)

    def post(self,request):

        total_marks  =  request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social_science']
        

        average_marks = total_marks / 5

        if((request.data['tamil'] >= 35) and (request.data['english'] >= 35) and (request.data['maths'] >= 35)and
           (request.data['science'] >= 35) and (request.data['social_science'] >= 35)):

            student_result = True

        else:
            student_result = False


        new_marks = RankSheet(tamil = request.data['tamil'], english = request.data['english'],
        maths = request.data['maths'],science = request.data['science'],social_science = request.data['social_science'],
        total = total_marks, average = average_marks, result = student_result)

        new_marks.save()

        return Response(
            {
                "message":"Marks Saved",
                "total" : total_marks,
                "average" :average_marks,
                "result" : student_result
            }
        )
    
    def patch(self,request,id):
        try:
            student = RankSheet.objects.get(id = id)
        except RankSheet.DoesNotExist:
            return Response({'error':'Student not found'},status=404)
        if('tamil' in request.data):
            student.tamil = request.data['tamil']
        if('english' in request.data):
            student.english = request.data['english']
        if('maths' in request.data):
            student.maths = request.data['maths']
        if('science' in request.data):
            student.science = request.data['science']
        if('social_science' in request.data):
            student.social_science = request.data['social_science']
        student.total = (
            student.tamil + student.english + student.maths + student.science + student.social_science
        )
        student.average = student.total/5

        if(
            student.tamil >= 35 and
            student.english >= 35 and
            student.maths >= 35 and
            student.science >= 35 and
            student.social_science >= 35
            
         ):
            student.result = True
        else:
            student.result = False

        student.save()
        return Response({
                "message":"Marks Saved",
                "total" : student.total,
                "average" :student.average,
                "result" : student.result
        })

    def put(self,request,id):
        try:
            student = RankSheet.objects.get(id = id)
        except RankSheet.DoesNotExist:
            return Response({'error':'Student not found'},status=404)
        if('tamil' in request.data):
            student.tamil = request.data['tamil']
        if('english' in request.data):
            student.english = request.data['english']
        if('maths' in request.data):
            student.maths = request.data['maths']
        if('science' in request.data):
            student.science = request.data['science']
        if('social_science' in request.data):
            student.social_science = request.data['social_science']
        student.total = (
            student.tamil + student.english + student.maths + student.science + student.social_science
        )
        student.average = student.total/5

        if(
            student.tamil >= 35 and
            student.english >= 35 and
            student.maths >= 35 and
            student.science >= 35 and
            student.social_science >= 35
            
         ):
            student.result = True
        else:
            student.result = False

        student.save()
        return Response({
                "message":"Marks Saved",
                "total" : student.total,
                "average" :student.average,
                "result" : student.result
        })
    
    def delete(self,request,id):

        marks = RankSheet.objects.get(id = id)

        marks.delete()

        return Response ("Marks Deleted")

    def patch(self,request,id):

        rank_data = RankSheet.objects.filter(id = id)

        total_marks  =  request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social_science']
        

        average_marks = total_marks / 5

        if((request.data['tamil'] >= 35) and (request.data['english'] >= 35) and (request.data['maths'] >= 35)and
           (request.data['science'] >= 35) and (request.data['social_science'] >= 35)):

            student_result = True

        else:
            student_result = False


        rank_data.update(tamil = request.data['tamil'], english = request.data['english'],
        maths = request.data['maths'],science = request.data['science'],social_science = request.data['social_science'],
        total = total_marks, average = average_marks, result = student_result)

        rank_data.save()

        return Response(
            {
                "message":"Marks Saved",
                "total" : total_marks,
                "average" :average_marks,
                "result" : student_result
            }
        )

    def put(self,request,id):

        rank_data = RankSheet.objects.filter(id = id)

        total_marks  =  request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social_science']
        

        average_marks = total_marks / 5

        if((request.data['tamil'] >= 35) and (request.data['english'] >= 35) and (request.data['maths'] >= 35)and
           (request.data['science'] >= 35) and (request.data['social_science'] >= 35)):

            student_result = True

        else:
            student_result = False


        rank_data.update(tamil = request.data['tamil'], english = request.data['english'],
        maths = request.data['maths'],science = request.data['science'],social_science = request.data['social_science'],
        total = total_marks, average = average_marks, result = student_result)

        rank_data.save()

        return Response(
            {
                "message":"Marks Saved",
                "total" : total_marks,
                "average" :average_marks,
                "result" : student_result
            }
        )

@api_view(['GET','POST'])
def task_list_create(request):

    if(request.method == "GET"):

        all_task = Task.objects.all()

        task_data = Task_Serializers(all_task,many = True).data

        return Response(task_data)
    
    elif(request.method == "POST"):

        new_task = Task_Serializers(data = request.data)
        
        if(new_task.is_valid()):
            new_task.save()
    
            return Response("New Task Added")
        else:
            return Response(new_task.errors)
@api_view(['GET','PATCH','PUT','DELETE'])
def task_update_delete(request,id):

    task = Task.objects.get(id = id )

    if(request.method == "GET"):

        task_data = Task_Serializers(task).data

        return Response(task_data)
    
    elif(request.method == "PATCH"):

        update_task = Task_Serializers(task,data = request.data, partial = True)

        if(update_task.is_valid()):

            update_task.save()
    
            return Response("Task updated")
        else:
            return Response(update_task.errors)
        
    elif(request.method == "PUT"):

        update_task = Task_Serializers(task,data = request.data, partial = True)

        if(update_task.is_valid()):

            update_task.save()
    
            return Response("Task updated")
        else:
            return Response(update_task.errors)
        
    elif(request.method == "DELETE"):

        task.delete()

        return Response ("Task Deleced")
