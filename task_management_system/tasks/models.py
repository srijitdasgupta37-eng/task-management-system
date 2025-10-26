from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_tasks')
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending','Pending'),('In Progress','In Progress'),('Completed','Completed')], default='Pending')
    file = models.FileField(upload_to='task_files/', null=True, blank=True)

    def __str__(self):
        return self.title