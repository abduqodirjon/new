from django.urls import path
from .views import student_all
urlpatterns = [
    path('', student_all, name="student_all"),
]
