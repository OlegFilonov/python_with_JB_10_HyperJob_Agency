from django.urls import path

from .views import CreateResumeView


urlpatterns = [
    path('resume/new', CreateResumeView.as_view())
]
