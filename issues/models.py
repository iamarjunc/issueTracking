# from django.db import models
# from users.models import CustomUser

# class Project(models.Model):
#     name = models.CharField(max_length=100)

# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     assignee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     completed = models.BooleanField(default=False)
#     reported_by = models.ForeignKey(CustomUser, related_name='reported_tasks', on_delete=models.CASCADE)
