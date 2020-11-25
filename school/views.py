from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Exam, Question
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
            current_exam.name = fields['Title']
            current_exam.start_date = fields['StartDate']
            current_exam.end_date = fields['EndDate']
            current_exam.save()
        elif request.POST['type'] == "Delete":
            Exam.objects.filter(pk=int(request.POST['deleteFormFieldid'])).delete()

        elif request.POST['type'] == "Add":
            exam = Exam(name=request.POST['addFormFieldTitle'], start_date=request.POST['addFormFieldStartDate'], end_date=request.POST['addFormFieldEndDate'])
            exam.save()

    return render(request, 'school/manage_exam.html', {'exams':exams})

def edit_exams(request, id):
    exam = get_object_or_404(Exam, pk=id)
    return render(request, 'school/edit_modal.html', {'exam':exam})

def delete_exams(request, id):
    exam = get_object_or_404(Exam, pk=id)
    return render(request, 'school/delete_modal.html', {'exam':exam})

def add_exams(request):
    # exam = get_object_or_404(Exam, pk=id)
    return render(request, 'school/add_modal.html')
