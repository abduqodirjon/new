from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    context = {}
    if request.method=="POST":
        fio = request.POST.get('fio')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        username = request.POST.get('username')
        parol = request.POST.get('parol')
        parol_1 = request.POST.get('parol_1')

        if len(fio)!=0 and len(tel)!=0 and len(email)!=0 and len(username) and len(parol)!=0 and len(parol_1):
            u = User.objects.filter(username=username)
            if len(u)==0:
                if parol==parol_1:
                    user = User.objects.create_user(first_name=fio, last_name=tel, email=email, username=username, password=parol)
                    user.save()
                    if user is not None:
                        return redirect('login')
                else:
                    context['error_2']="Parollar mos kelmadi"
            else:
                context['error_1']="Bunday Username mavjud iltimos boshqa username kiriting"
        else:
            context['error']="Ma'lumotlarni to'ldiring"
    return render(request, 'registration/signup.html', context)

def log_in(request):
    context = {}
    if request.method=="POST":
        username = request.POST.get('username')
        parol = request.POST.get('parol')
        if len(username) and len(parol)!=0:
            user = authenticate(request, username=username, password = parol)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context['error']="Username yoki parol xato"
        else:
            context['error']="Ma'lumotlarni to'ldiring"
    return render(request, 'registration/login.html', context)


def log_out(request):
    if request.method=="GET":
        logout(request)
        return redirect('home')

