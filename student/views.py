from django.http import request
from django.shortcuts import render
from .models import Students
from django.contrib.auth.decorators import login_required


# Create your views here.

def student_all(request):
    context = {}
    context['info'] = Students.objects.all()
    return render(request, 'student/student_all.html', context)