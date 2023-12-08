from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Task
from api.serializers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class=TaskSerializer
    
    #companies/{companyId}/emplyees
   
