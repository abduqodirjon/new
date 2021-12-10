from django import forms
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .forms import CustomCreateUserForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib import messages

# Create your views here.
@unauthenticated_user
def signup(request):
    context = {}
    form = CustomCreateUserForm(request.POST, request.FILES)
  
    if request.method=="POST":
        inf = CustomUser.objects.filter(username=form['username'].value())
        
        print(form['password1'].value()==form['password2'].value())
        print(form.is_valid())
        
        if len(inf)==0:
            if len(form['password1'].value())>=8 and len(form['password1'].value())>=8:
                if (form['password1'].value()==form['password2'].value()):
                    if form.is_valid():
                        user = form.save()
                        username = form.cleaned_data.get('username')
                        messages.success(request, username+' uchun profil yaratildi')
                        group = Group.objects.get(name='foydalanuvchi')
                        user.groups.add(group)
                        return redirect('login')
                    else:
                        context['password_error'] = "Siz kiritgan Parol juda keng tarqalgan, iltimos boshqa parol kiriting"
                else:
                    context['password_error'] = "Parollar bir-biri bilan mos kelmadi, iltimos boshqa parol kiriting"

            else:
                context['password_error'] = "Parol uzunligi kamida 8 ta katta yoki kichik harflar va raqamlardan iborat bo'lishi kerak, iltimos boshqa parol kiriting"
        else:
            context['user_error'] = "Siz kiritgan Username mavjud, iltimos boshqa username kiriting"
    

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
def user_detail(request):
    context = {}
    if request.user.is_authenticated:
        context['users'] = CustomUser.objects.get(username=request.user.username) 
  
    return render(request, 'registration/user_detail.html', context)

@login_required(login_url='login')
def edit_profil(request):
    context = {}
    if request.user.is_authenticated:
        context['users'] = CustomUser.objects.get(username=request.user.username) 
        form = CustomUserChangeForm(instance=request.user)
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid() :
                form.save()
                return redirect('user_detail')
        context['form'] = form
  
    return render(request, 'registration/edit_profil.html', context)

