from django import forms
from django.shortcuts import render, redirect
from .models import Category, News
from . import forms
# Create your views here.

def yangilik(request):
    context = {}
    context['news'] = News.objects.all()
    return render(request, 'yangilik/yangilik.html', context)

def yan_add_test(request):
    context = {}
    if request.method == "POST":
        form = forms.NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance

        return render(request, 'yangilik/yan_add_test.html', {'form': form, 'img_obj': img_obj})
    else:
        form = forms.NewsForm()
    return render(request, 'yangilik/yan_add_test.html', {'form': form})


def yan_add(request):
    context = {}
    context['categorys'] = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        img = request.POST.get('img')
        text_full = request.POST.get('text_full')
        print(img)
        if title != "" and content != "" and category != 0 and text_full != "":
            ctg = Category.objects.get(id=category)
            new = News(title=title, content=context, category=ctg, image=img, text_full=text_full)
            new.save()
        return redirect('yangilik')

   

    return render(request, 'yangilik/yan_add.html', context)

def edit(request, pk):
    context = {}
    context['categorys'] = Category.objects.all()
    context['edit'] = News.objects.get(id=pk)
    return render(request, 'yangilik/yan_add.html', context)

def delete(request, pk):
    context = {}
    context['edit'] = News.objects.get(id=pk)
    return render(request, 'yangilik/yangilik.html', context)

