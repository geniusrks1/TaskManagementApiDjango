from rest_framework import serializers
from api.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    task_id=serializers.ReadOnlyField()
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
   
    class Meta:
        model = Task
        fields="__all__"
