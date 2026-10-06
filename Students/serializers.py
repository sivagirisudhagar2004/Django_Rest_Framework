from rest_framework.serializers import ModelSerializer
from .models import Task


class Task_Serializers(ModelSerializer):

    class Meta:

        model = Task
        fields = "__all__"