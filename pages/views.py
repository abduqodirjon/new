from django.shortcuts import render
from news.models import Category, News

# Create your views here.
def index(request):
    context = {}
    context['news'] = News.objects.all()
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def natija(request):
    return render(request, 'natija.html')

def statistika(request):
    return render(request, 'statistika.html')

def contact(request):
    return render(request, 'contact.html')