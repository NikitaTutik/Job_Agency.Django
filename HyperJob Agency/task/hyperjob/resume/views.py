from django.shortcuts import render
from django.views import View
from .models import User, Resume
from django.db import models


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        context = {"resumes": resumes}
        return render(request, 'resume/resumes.html', context)
