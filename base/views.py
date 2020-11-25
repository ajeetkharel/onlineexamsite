from django.shortcuts import render

def home(request):
    context = {
        'title':"Dashboard"
    }
    return render(request, 'base/dashboard.html', context=context)