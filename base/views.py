from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
    context = {
        'title':"Dashboard"
    }
    return render(request, 'base/dashboard.html', context=context)