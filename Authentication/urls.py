from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpattarns = [
    path('user/',UserView.as_view()),
    path('login/',UserLoginView.as_view()),
    
]

