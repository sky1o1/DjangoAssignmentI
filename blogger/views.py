from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AuthorForm, BlogForm
from .models import Author, BlogTable


def home_view(request):
    return render(request, 'blogger/home.html')


def create_view(request):
    auth_form = AuthorForm()
    blog_form = BlogForm()
    if request.method == 'POST':
        auth_form = AuthorForm(request.POST)
        blog_form = BlogForm(request.POST)
        if auth_form.is_valid() and blog_form.is_valid():
            auth_form.save()
            blog_form.save()
            print("successfully saved")
            return redirect('/blog/home/')
        else:
            return HttpResponse("Form is not valid")
    return render(request, 'blogger/create.html/', {'form1': auth_form, 'form2': blog_form})


def list_view(request):
    model_form = BlogTable.objects.all()
    print(model_form)
    context = {
        'data': model_form,
    }
    return render(request, 'blogger/list.html/', context)


