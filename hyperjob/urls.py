"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .views import MainPage, MyLoginView, MySignUp, ProfilePage
from resume.views import ResumeList, ResumeNew
from vacancy.views import VacanciesList, VacancyNew
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view()),
    path('resumes', ResumeList.as_view()),
    path('vacancies', VacanciesList.as_view()),
    path('login', MyLoginView.as_view()),
    path('signup', MySignUp.as_view()),
    path('logout', LogoutView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('resume/new', ResumeNew.as_view()),
    path('vacancy/new', VacancyNew.as_view()),
    path('home', ProfilePage.as_view())
]

# from django.contrib import admin
# from django.urls import path, include
# from . import views
# from .views import VacancyCreateView, ResumeCreateView
# from resume.views import *
# from vacancy.views import *

#
# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import RedirectView
# from .views import *
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', MainPageView.as_view()),
#     path('resumes', include('resume.urls')),
#     path('vacancies', include('vacancy.urls')),
#     path('', include('resume.urls2')),
#     path('', include('vacancy.urls2')),
#     path('login', MyLoginView.as_view()),
#     path('signup', MySignupView.as_view()),
#     path('login/', RedirectView.as_view(url='/login')),
#     path('signup/', RedirectView.as_view(url='/signup')),
#     path('home', HomePage.as_view()),
# ]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.MainPageView.as_view()),
#     path('vacancies/', include('vacancy.urls')),
#     path('resumes/', include('resume.urls'))
# ]
#
# urlpatterns += [

#     path('home', views.HomePage.as_view())
# ]
#
# urlpatterns += [
#     path('resume/new', ResumeCreateView.as_view()),
#     path('vacancy/new', VacancyCreateView.as_view())
# ]
