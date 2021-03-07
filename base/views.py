from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import pytz

from school.models import Student, Class, Exam

@login_required()
def home(request):
    context = {
        'title':"Dashboard"
    }
    current_exam = None
    if request.user.is_student:
        student = Student.objects.get(user=request.user)
        exams = Exam.objects.filter(assigned_class=student.reading_class)
        context["current_exams"] = []
        context["exams"] = []
        if exams:
            today_date = datetime.now().replace(tzinfo=pytz.UTC) + timedelta(hours=5, minutes=45) 
            for exam in exams:
                if exam.start_date.day == today_date.day:
                    context["current_exams"].append(exam)
                else:
                    context["exams"].append(exam)
        return render(request, 'base/dashboard.html', context=context)
    else:
        return render(request, 'base/dashboard.html', context=context)

