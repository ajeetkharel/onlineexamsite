from django.contrib import admin
from school.models import Exam, Question, Class, Student, Result

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Result)