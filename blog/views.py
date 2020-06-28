from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post,Blogcomment
from django.contrib import messages
# Create your views here.


def index(request):
    allposts=Post.objects.all()
    context = {'allposts':allposts}
    return render(request, 'blog/index.html',context)


def blogPost(request,slug):
    posts=Post.objects.filter(slug=slug).first()
    comments=Blogcomment.objects.filter(post=posts)
    if posts != None:
        context = {'post':posts,'comments':comments}
    else:
        return HttpResponse('error')
    return render(request, 'blog/blogpost.html',context)

def postcomment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post=Post.objects.get(s_no=postSno)
        csave = Blogcomment(comment=comment,user=user,post=post)
        csave.save()
        messages.success(request, "your post has been posted successfully")
    return redirect(f'/blog/{post.slug}')

