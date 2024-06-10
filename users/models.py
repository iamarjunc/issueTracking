from django.db import models
from django.contrib.auth.models import AbstractUser
from issueTracking import settings

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Developer', 'Developer'),
        ('Functional', 'Functional'),
        ('Tester', 'Tester'),
        ('Admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, default='Developer', choices=USER_TYPE_CHOICES)

class Project(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='projects')

    def __str__(self):
        return self.name

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    module = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=50)
    problem = models.TextField()
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.issue_type} - {self.created_at}"
