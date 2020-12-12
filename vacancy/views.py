from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from django.http import HttpResponseForbidden

# Create your views here.

class VacanciesList(View):
    def get(self, request):
        return render(request, "vacancy/vacancy_list.html", {'vacancy': Vacancy.objects.all()})

class VacancyNew(View):
    def get(self, request):
        if not request.user.is_authenticated or request.user.is_staff != True:
            return HttpResponseForbidden()
        else:
            return render(request,"vacancy/vacancy_new.html")

    def post(self, request):
        if request.user.is_staff != True:
            return HttpResponseForbidden()
        else:
            description = request.POST.get('description')
            Vacancy.objects.create(author=request.user, description=description)
            return redirect('/home')

#
#
# from django.shortcuts import render, redirect
# from .models import Vacancy
# from django.views.generic import TemplateView
# from django.views import View
# from django import forms
# from django.http import HttpResponseForbidden
# from django.contrib.auth.models import User
#
#
# class CreateVacancyForm(forms.Form):
#     description = forms.CharField(label="Description")
#
#
# class VacancyView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         vacancies = Vacancy.objects.all()
#         return render(request, 'vacancy/vacancies.html', context={'vacancies': vacancies})
#
#
# class CreateVacancyView(View):
#
#     def get(self, request):
#         if not request.user.is_authenticated or request.user.is_staff != True:
#             return HttpResponseForbidden()
#         else:
#             return render(request,"vacancy/create_vacancy.html")
#
#     def post(self, request):
#         if request.user.is_staff != True:
#             return HttpResponseForbidden()
#         else:
#             description = request.POST.get('description')
#             Vacancy.objects.create(author=request.user, description=description)
#             return redirect('/home')


