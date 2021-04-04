from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Exam, Question, Class, Result, Student
from user.models import User
from datetime import datetime, timedelta
from django.shortcuts import get_list_or_404, get_object_or_404
import pytz
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def manage_exams(request):
    exams = Exam.objects.all()
    if request.method == 'POST':

        if request.POST['type'] == "Edit":
            fields = {}
            for key, value in request.POST.items():
                if key.startswith("editFormField"):
                    fields[key[13:]] = value
            current_exam = exams.filter(pk=int(fields['id']))[0]
            current_exam.subject = fields['Title']
            current_exam.start_date = fields['StartDate']
            current_exam.end_date = fields['EndDate']
            current_exam.save()

        elif request.POST['type'] == "Delete":
            Exam.objects.filter(pk=int(request.POST['deleteFormFieldid'])).delete()

        elif request.POST['type'] == "Add":
            exam = Exam(subject=request.POST['addFormFieldTitle'], 
                        start_date=request.POST['addFormFieldStartDate'], 
                        end_date=request.POST['addFormFieldEndDate'],
                        assigned_class_id=request.POST["addFormFieldClass"])
            exam.save()

    return render(request, 'school/manage_exam.html', {'exams':exams})

def edit_exams(request, id):
    exam = get_object_or_404(Exam, pk=id)
    return render(request, 'school/edit_modal.html', {'exam':exam})

def delete_exams(request, id):
    exam = get_object_or_404(Exam, pk=id)
    return render(request, 'school/delete_modal.html', {'exam':exam})

def add_exams(request):
    context = {
        "classes": Class.objects.all()
    }
    return render(request, 'school/add_modal.html', context=context)


def take_exam(request, pk):
    student = Student.objects.get(user=request.user)
    exam = Exam.objects.get(pk=pk)
    questions = Question.objects.filter(exam=exam)

    context = {
        'title': f"{exam.subject} Exam",
        'Exam': exam,
        'questions': questions,
        'taken': False
    }
    if Result.objects.filter(student=student, exam=exam).exists():
        context["taken"] = True
        context['result'] = Result.objects.get(student=student, exam=exam)
    else:
        if request.method == "POST":
            correct = 0
            for i in range(questions.count()):
                user_answer = int(request.POST['question'+str(questions[i].pk)])
                correct_answer = questions[i].answer
                if user_answer == correct_answer:
                    correct+=1
            Result.objects.create(exam=exam, student=student, marks=correct)
            context["taken"] = True
    return render(request, "school/exam_view.html", context=context)
 

def get_results(request, examid):
    exam = Exam.objects.get(pk=examid)
    results = Result.objects.filter(exam=exam)
    return render(request, "base/results.html", context={'results': results})

def make_available(request, resultid):
    if request.method == "POST":
        result = Result.objects.get(pk=resultid)
        if request.POST["type"] == "hide":
            result.available = False
        else:
            result.available = True
        result.save()
        return HttpResponse("success")

def student_results(request):
    results = Result.objects.filter(student=Student.objects.get(user=request.user))

    context = {
        'title': "Student Results",
        'results': results,
    }
    return render(request, "school/student_results.html", context = context)