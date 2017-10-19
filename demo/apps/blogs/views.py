  # views.py
from django.shortcuts import render, HttpResponse, redirect
from .models import Blog
from django.core.urlresolvers import reverse

def index(request):
    return render(request, "blogs/index.html", {"blogs": Blog.objects.all() })

def update(request):
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/blog/edit/'+id)
    else:
        blog = Blog.objects.get(id = id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        return redirect('/blogs')

def index(request):
    print("hello, I am your first request")
    return redirect('/target/this_app/new')


def index(request):
   print("hello, I am your first request")
   return redirect(reverse('my_new'))