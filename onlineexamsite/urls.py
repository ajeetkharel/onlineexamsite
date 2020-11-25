"""onlineexamsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as userviews
from django.conf import settings
from django.conf.urls.static import static
from school import views as schoolviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('login/', userviews.login_user, name='login'),
    path('register/', userviews.register_user, name='register'),
    path('logout/', userviews.logout_user, name='logout'),
    
    path('manage_exams/', schoolviews.manage_exams, name='exam-manage'),
    path('manage_exams/edit_exams/<int:id>/', schoolviews.edit_exams, name='edit-exam'),
    path('manage_exams/delete_exams/<int:id>/', schoolviews.delete_exams, name='delete-exam'),
    path('manage_exams/add_exams/', schoolviews.add_exams, name='add-exam'),
]

admin.site.enable_nav_sidebar = True

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL ,document_root=settings.STATIC_ROOT)
