from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Task
from api.serializers import TaskSerializer



# from rest_framework import permissions
# from rest_framework.permissions import IsAuthenticated, IsOwnerOrReadOnly

# class IsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # Write permissions are only allowed to the owner of the task
#         return obj.owner == request.user







# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class=TaskSerializer
  



    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    

   
