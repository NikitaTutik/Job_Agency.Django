from django.shortcuts import render
from django.views import View
from .models import User, Vacancy
from django.db import models

# Create your views here.


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        context = {"vacancies": vacancies}
        return render(request, 'vacancy/vacancies.html', context)
