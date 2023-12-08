from django.db import models
from django.contrib.auth.models import User  # Import User model
# Create your models here.
# creating task model

class Task(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    task_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
