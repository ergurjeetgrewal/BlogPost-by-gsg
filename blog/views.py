from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.


def index(request):
    allposts=Post.objects.all()
    context = {'allposts':allposts}
    return render(request, 'blog/index.html',context)


def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    if post != None:
        context = {'post':post}
    else:
        return HttpResponse('error')
    print(context)
    return render(request, 'blog/blogpost.html',context)
