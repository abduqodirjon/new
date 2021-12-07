from django.shortcuts import render
from news.models import Category, News
from django.contrib.auth.decorators import login_required
from registration.models import CustomUser


# Create your views here.
def index(request):
    context = {}
    context['news'] = News.objects.all()
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
@login_required(login_url='login')
def natija(request):
    return render(request, 'natija.html')

@login_required(login_url='login')
def statistika(request):
    return render(request, 'statistika.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')