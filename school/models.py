from django.db import models
from django.utils import timezone

class Exam(models.Model):
    name = models.CharField(max_length=255, default='')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

class Question(models.Model):
    title = models.CharField(max_length=255, default='')
    option1 = models.CharField(max_length=255, default='')
    option2 = models.CharField(max_length=255, default='')
    option3 = models.CharField(max_length=255, default='')
    option4 = models.CharField(max_length=255, default='')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)