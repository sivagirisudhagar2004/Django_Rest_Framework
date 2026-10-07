from rest_framework.serializers import ModelSerializer
from .models import *


class Task_Serializers(ModelSerializer):

    class Meta:

        model = Task
        fields = "__all__"

class RankSheet_Serilizes(ModelSerializer):

    class Meta:
        model = RankSheet
        fields = '__all__'

class Student_Task_Serializer(ModelSerializer):

    all_task = Task_Serializers( many = True)

    class Meta:
        model = Student
        fields = '__all__'

