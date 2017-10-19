from __future__ import unicode_literals 
from django.shortcuts import render
from . models import Author

def index(request):
    my_book = Author.objects.create(name="Little Women")
    print my_book
    context = {"authors": Author.objects.all()}
    return render(request, "index.html", context)