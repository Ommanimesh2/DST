from django.contrib import admin
from django.urls import path
from .views import JobView,UpdateJobView

urlpatterns = [
    path("rent/", JobView.as_view()),
    path("job/<int:pk>", UpdateJobView.as_view()),
]
