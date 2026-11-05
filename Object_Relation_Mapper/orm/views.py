from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Sum,Avg,Max,Min,Q,Count


class StudentView(APIView):
    def get(self,request):
        return Response()




