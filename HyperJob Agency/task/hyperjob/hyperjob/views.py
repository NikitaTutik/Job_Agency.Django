from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.core.exceptions import PermissionDenied
from django import forms
from resume.models import Resume
from vacancy.models import Vacancy


# Create your views here.
class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')


class MySignUpView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    success_url = '/'
    template_name = 'login.html'


class NewPost(forms.Form):
    description = forms.CharField(min_length=10, max_length=1024)


class NewResume(View):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.user.username)[0]
        description = request.POST.get('description')
        Resume.objects.create(author=user, description=description)
        return redirect('/home')


class NewVacancy(View):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.user.username)[0]
        description = request.POST.get('description')
        if user.is_staff:
            Vacancy.objects.create(author=user, description=description)
            return redirect('/home')
        raise PermissionDenied


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        new_post = NewPost()
        context = {"form": new_post}
        return render(request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.filter(username=request.user.username)[0]
            if user.is_staff:
                return redirect('/vacancy/new')
            else:
                return redirect('/resume/new')
        else:
            raise PermissionDenied
