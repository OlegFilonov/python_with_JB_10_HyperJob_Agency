from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
from django.http import HttpResponseForbidden


# Create your views here.

class ResumeList(View):
    def get(self, request):
        return render(request, "resume/resume_list.html", {'resume': Resume.objects.all()})

class ResumeNew(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            return render(request,"resume/resume_new.html")

    def post(self, request):
        description = request.POST.get("description")
        Resume.objects.create(author=request.user, description=description)
        return redirect('/home')

# # from django.shortcuts import render, redirect
# # from .models import Resume
# from django.views.generic import TemplateView
# # from django import forms
# # from django.http import HttpResponseForbidden
# # from django.views import View
# # from django.contrib.auth.models import User
#
# from django.shortcuts import render, redirect
# from django.views import View
# from .models import Resume
# from django.http import HttpResponseForbidden
#
#
# class ResumeView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         resumes = Resume.objects.all()
#         return render(request, 'resume/resumes.html', context={'resumes': resumes})


# class CreateResumeForm(forms.Form):
#     description = forms.CharField(label="Description")

#
# class CreateResumeView(View):
#     def get(self, request):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         else:
#             return render(request, "resume/create_resume.html")
#
#     def post(self, request):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         else:
#             description = request.POST.get("description")
#             Resume.objects.create(author=request.user, description=description)
#             return redirect('/home')

    #
    # def get(self, request):
    #     form = CreateResumeForm()
    #     return render(request, "resume/create_resume.html", context={'form': form})
    #
    # def post(self, request):
    #     form = CreateResumeForm(request.POST)
    #     if form.is_valid():
    #         if not request.user.is_staff:
    #             Resume.objects.create(description=request.POST.get("description"), author=request.user)
    #             return redirect('/home')
    #         else:
    #             return HttpResponseForbidden('<h1>403 Forbidden</h1>', content_type='text/html')
    #     else:
    #         return HttpResponseForbidden('<h1>403 Forbidden</h1>', content_type='text/html')
