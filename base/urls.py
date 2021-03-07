from django.contrib import admin
from django.urls import path, include

from base.views import home
from school.views import *

urlpatterns = [
    path('', home, name="home"),
    path('exams/<pk>', take_exam, name="take-exam")
]