from django import forms
from django.shortcuts import render, redirect
from .models import Category, News
from .forms import NewsForm
from registration.decorators import allowed_users
# Create your views here.

def yangilik(request):
    context = {}
    context['news'] = News.objects.all()
    return render(request, 'yangilik/yangilik.html', context)


@allowed_users(allowed_roles=['admin'])
def yan_add(request):
    context = {}
    context['categorys'] = Category.objects.all()
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['news'] = News.objects.all()
            return redirect('yangilik')
    context['form'] = NewsForm()
    return render(request, 'yangilik/yan_add.html', context)

@allowed_users(allowed_roles=['admin'])
def edit(request, pk):
    context = {}
    new = News.objects.get(id=pk)
    form = NewsForm(instance=new)
    if request.method == "POST":
        print("salom")
        form = NewsForm(request.POST, instance=new)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('yangilik')
    context['form'] = form
    return render(request, 'yangilik/yan_add.html', context)

@allowed_users(allowed_roles=['admin'])
def delete(request, pk):
    form = News.objects.get(id=pk)
    if request.method == "POST":
        form.delete()
        return redirect('yangilik')
    return render(request, 'yangilik/yan_delete.html', {'form':form})

