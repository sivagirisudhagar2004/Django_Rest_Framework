from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import*
from rest_framework import status
from django.contrib.auth import authenticate

# Create your views here.

class UserView(APIView):

    def post(self,request):

        new_user = User(username = request.data['username'],is_superuser = request.data['is_superuser'])

        new_user.set_password(request.data['password'])

        new_user.save()

        return Response("New User Updated", status=200)

class UserLoginView(APIView):

    def post(self,request):

        user_Authentication = authenticate(username = request.data['username'],password = request.data['password'] )

        #print(user_Authentication.username)

        if(user_Authentication == None):

            return Response( "User and Password  is Unvaild , Please Try again..!! ",status=502)
        else:

            return Response(" Valid User..!!",status=200)

 