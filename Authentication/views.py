from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import*
from rest_framework import status
from django.contrib.auth import authenticate

# Create your views here.

class UserView(APIView):

    def post(self,request):

        new_user = User(username = request.data['name'],is_superuser = request.data['is_superuser'])

        new_user.set_password(password = request.data['password'])

        new_user.save()

        return Response("New User Updated", status=200)

class UserLoginView(APIView):

    def post(self,request):

        user_Authentication = authenticate(username = request.data['username'] )

        print(user_Authentication.date_joined)

        if(user_Authentication == None):

            return Response( "User and Password  is Unvaild , Please Try again..!! ")
        else:

            return Response(" Valid User..!!")

 