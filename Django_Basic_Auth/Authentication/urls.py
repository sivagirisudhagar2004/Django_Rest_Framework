from django.urls import path
from .views import *

urlpatterns = [
    path("api/",Testview.as_view())
]