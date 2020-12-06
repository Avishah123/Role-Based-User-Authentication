
from django.contrib import admin
from django.urls import path, include
from .views import StudentSignUpView, TeacherSignUpView


urlpatterns = [
    path('students', StudentSignUpView.as_view(), name='student1'),
    path('teacher', TeacherSignUpView.as_view(), name='teacher1'),

]
