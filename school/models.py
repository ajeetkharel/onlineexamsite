from django.db import models
from django.utils import timezone

from user.models import User

class Class(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reading_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.email


class Exam(models.Model):
    subject = models.CharField(max_length=255, default='')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject


class Question(models.Model):
    title = models.CharField(max_length=255, default='')
    option1 = models.CharField(max_length=255, default='')
    option2 = models.CharField(max_length=255, default='')
    option3 = models.CharField(max_length=255, default='')
    option4 = models.CharField(max_length=255, default='')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{{self.exam}} question"


class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{{self.student}} {{self.exam}} marks"