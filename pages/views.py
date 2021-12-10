from django.shortcuts import redirect, render
from news.models import Category, News
from django.contrib.auth.decorators import login_required
from registration.models import CustomUser


# Create your views here.
def base(request):
    if request.user.is_authenticated:
        usr = CustomUser.objects.get(username=request.user.username)
        print(usr)
        return render(request, base.html, {'usr': usr})
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

def admin(request):

    return render(request, 'admin/main.html')