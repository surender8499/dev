from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100, null=True)

    description = models.CharField(max_length=1000, null=True, blank=True)

    status = models.CharField(max_length=25)

    due_date = models.DateField(null=True, blank=True)

    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
