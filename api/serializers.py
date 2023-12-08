from rest_framework import serializers
from api.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    task_id=serializers.ReadOnlyField()
    class Meta:
        model = Task
        fields="__all__"
