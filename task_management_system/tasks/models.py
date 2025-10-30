from django.db import models
from accounts.models import CustomUser

class Task(models.Model):
    PRIORITY_CHOICES = [('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]
    STATUS_CHOICES = [('Pending', 'Pending'), ('In-Progress', 'In-Progress'), ('Completed', 'Completed')]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_tasks')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)