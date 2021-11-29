from django import forms
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .forms import CreateUserForm

# Create your views here.
@unauthenticated_user
def signup(request):
    context = {}
    form = CreateUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')

        group = Group.objects.get(name='foydalanuvchi')
        user.groups.add(group)
        messages.success(request, "Profil yaratildi" + username)
        return redirect('login')
    context['form'] = form
    return render(request, 'registration/signup.html', context)


@unauthenticated_user
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
@login_required(login_url='login')
def edit_profil(request):
    context = {}

    return render(request, 'registration/edit_profil.html')

