from django.urls import path
from .views import teacher_all
urlpatterns = [
    path('', teacher_all, name='teacher_all')
]
