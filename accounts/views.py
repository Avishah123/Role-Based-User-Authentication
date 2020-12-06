from django.shortcuts import render, redirect
from .forms import StudentSignUpForm, TeacherSignUpForm
from .models import Student, Teacher, User
from django.views.generic import CreateView
from django.contrib.auth import login

# Create your views here.


def home(request):
    return render(request, 'home.html')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user-type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'forms/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user-type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()

        return redirect('home')
