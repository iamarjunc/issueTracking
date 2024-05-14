from django.db import models
from django.contrib.auth.models import User 

class Project(models.Model):
    name = models.CharField(max_length=255)

    # Additional fields and methods can be added here as needed

    def __str__(self):
        return self.name
    
class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    module = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=50)
    problem = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.issue_type} - {self.created_at}"