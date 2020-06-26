from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def blogPost(request,slug):
    # return HttpResponse(f'this is blog {slug}')
    return render(request, 'blog/blogpost.html',{'params':slug})
