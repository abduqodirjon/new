from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import Category, News
from .forms import NewsForm
from registration.decorators import allowed_users
from django import forms


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
            form.instance.author = request.user
            form.save()
            # n = News.objects.create(author=request.user)
            # n.save()
            # print(n.author)
            # print(request.user.username)
          
            
            context['news'] = News.objects.all()
            return redirect('yangilik')
    context['form'] = NewsForm()
    return render(request, 'yangilik/yan_add.html', context)



@allowed_users(allowed_roles=['admin'])
def edit(request, pk):
    context = {}
    new = News.objects.get(id=pk)

    if str(request.user)==str(new.author):
        form = NewsForm(instance=new)
        if request.method == "POST":
            form = NewsForm(request.POST, request.FILES, instance=new)
            if form.is_valid():
                form.save()
                return redirect('yangilik')
    else:
        return HttpResponse("<center><br><br><h3>Siz bu maqolaning muallafi emassiz.</h3><h1> Ruxsat yo'q !</h1></center>")
    context['form'] = form
    return render(request, 'yangilik/yan_add.html', context)



@allowed_users(allowed_roles=['admin'])
def delete(request, pk):
    form = News.objects.get(id=pk)
    if str(request.user)==str(form.author):
        if request.method == "POST":
            form.delete()
            return redirect('yangilik')
    else:
        return HttpResponse("<center><br><br><h3>Siz bu maqolaning muallafi emassiz.</h3><h1> Ruxsat yo'q !</h1></center>")
    return render(request, 'yangilik/yan_delete.html', {'form':form})

