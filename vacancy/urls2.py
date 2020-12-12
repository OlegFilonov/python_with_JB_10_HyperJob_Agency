from django.urls import path

from .views import VacancyView


urlpatterns = [
    path('vacancy/new', VacancyView.as_view()),
]
