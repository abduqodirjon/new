from django.shortcuts import render

# Create your views here.
def teacher_all(request):
    context ={}

    return render(request, 'teacher/teacher_all.html', context)