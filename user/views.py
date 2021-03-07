from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout

from school.models import Student, Class

def login_user(request):
    context = {
        'title': "Login"
    }
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context['message'] = "Invalid email/password"
        return render(request, 'user/login.html', context=context)

def register_user(request):
    context = {
        'title': "Login",
        "classes": Class.objects.all()
    }
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                email = request.POST["email"]
                password = request.POST["password1"]
                user = authenticate(request, email=email, password=password)

                student = Student(user=user, reading_class_id=request.POST["class"])
                student.save()

                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    print("Registration failed")
            return render(request, 'user/register.html', context={'form':form, 'title':"Register", "classes": Class.objects.all()})
    return render(request, 'user/register.html', context=context)
    
def logout_user(request):
    logout(request)
    return redirect('login')